#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 2018/6/11 20:22

from nanotime import nanotime
from numpy import random


def is_amicable_number(num):
    # sum all divisor, except itself
    left_divisor_sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            left_divisor_sum += i
    # assume num and left_divisor_sum are amicable pair
    # so the all divisor sum(except itself) is equal to num
    right_divisor_sum = 0
    for j in range(1, left_divisor_sum // 2 + 1):
        if left_divisor_sum % j == 0:
            right_divisor_sum += j
    if right_divisor_sum == num and num != left_divisor_sum:
        return num, left_divisor_sum
    return None


def amicable_pair_in_range(num):
    """
        seek all amicable pair from 1 to num
    :param num:
    :return:
    """
    for i in range(1, num):
        amicable_pair = is_amicable_number(i)
        if isinstance(amicable_pair, tuple):
            print(amicable_pair)


def seek_amicable(ceiling):
    """
        advanced version
    :param ceiling:
    :return:
    """
    # save the true factor sum
    # 1 is the true factor of all natural numbers, so initialization is 1
    sum_list = [1 for i in range(ceiling + 1)]
    for i in range(2, ceiling // 2 + 1):
        # ignore itself, start next
        j = 2 * i
        while j <= ceiling:
            sum_list[j] += i
            # print("sum_list[%d] = %d" % (j, sum_list[j]))
            j += i
    # The minimum known amicable number is 220
    # So starting from 220
    for i in range(220, ceiling):
        if ceiling >= sum_list[i] > i == sum_list[sum_list[i]]:
            print("( %d, %d )" % (i, sum_list[i]))


def bubble_sort(unordered_set):
    """

    :param unordered_set:
    :return:
    """
    set_len = len(unordered_set)
    for i in range(set_len):
        for j in range(i, set_len):
            if unordered_set[i] < unordered_set[j]:
                # change each other
                unordered_set[i], unordered_set[j] = unordered_set[j], unordered_set[i]
    # for clear semantics
    ordered_list = unordered_set
    return ordered_list


def selection_sort(unordered_set):
    """

    :param unordered_set:
    :return:
    """
    set_len = len(unordered_set)
    for i in range(set_len):
        # assume the first one is the maximum
        assume_max_idx = i
        max_val = unordered_set[assume_max_idx]
        for j in range(i + 1, set_len):
            if max_val < unordered_set[j]:
                assume_max_idx = j
                max_val = unordered_set[assume_max_idx]
        # change each other
        unordered_set[i], unordered_set[assume_max_idx] = unordered_set[assume_max_idx], unordered_set[i]
    # for clear semantics
    ordered_list = unordered_set
    return ordered_list


def insertion_sort(unordered_set):
    """

    :param unordered_set:
    :return:
    """
    set_len = len(unordered_set)
    for i in range(set_len):
        # Use slices to implement reverse traversal
        for j in range(i)[::-1]:
            if unordered_set[j + 1] < unordered_set[j]:
                unordered_set[j], unordered_set[j + 1] = unordered_set[j + 1], unordered_set[j]
            else:
                break
    # for clear semantics
    ordered_list = unordered_set
    return ordered_list


def quick_sort(array):
    """

    :param array:
    :return:
    """
    arr_len = len(array)
    if arr_len <= 1:
        return array
    # num = array[0]
    num = array[random.randint(arr_len)]
    less = [i for i in array[1:] if i <= num]
    greater = [i for i in array[1:] if i > num]
    return quick_sort(less) + [num] + quick_sort(greater)


def shell_sort(array):
    """

    :param array:
    :return:
    """
    step = len(array) // 2
    while step > 0:
        for i in range(step, len(array)):
            while i >= step and array[i] < array[i - step]:
                array[i], array[i - step] = array[i - step], array[i]
                i -= step
        step //= 2
    return array


if __name__ == '__main__':
    # amicable_pair_in_range(3000)
    # seek_amicable(3000)

    unsort_list = random.randint(1000, size=100)
    print(unsort_list)

    # start_time = nanotime.nanoseconds(nanotime.now())
    # sorted_list = bubble_sort(unsort_list)
    # end_time = nanotime.nanoseconds(nanotime.now())
    # print('Bubble sort Used time: %dns' % (end_time - start_time))

    # start_time = nanotime.nanoseconds(nanotime.now())
    # sorted_list = selection_sort(unsort_list)
    # end_time = nanotime.nanoseconds(nanotime.now())
    # print('Selection sort Used time: %dns' % (end_time - start_time))

    # start_time = nanotime.nanoseconds(nanotime.now())
    # sorted_list = insertion_sort(unsort_list)
    # end_time = nanotime.nanoseconds(nanotime.now())
    # print('Insertion sort Used time: %dns' % (end_time - start_time))

    # start_time = nanotime.nanoseconds(nanotime.now())
    # sorted_list = quick_sort(unsort_list)
    # end_time = nanotime.nanoseconds(nanotime.now())
    # print('Quick sort Used time: %dns' % (end_time - start_time))

    start_time = nanotime.nanoseconds(nanotime.now())
    sorted_list = shell_sort(unsort_list)
    end_time = nanotime.nanoseconds(nanotime.now())
    print('Shell sort Used time: %dns' % (end_time - start_time))

    print(sorted_list)
