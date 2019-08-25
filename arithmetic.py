#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 2018/6/11 20:22
from collections import deque
from functools import reduce

from numpy import random, math


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
        quick sort
    :param array:
    :return:
    """
    arr_len = len(array)
    if arr_len <= 1:
        return array
    rand_val = random.randint(arr_len)
    num = array[rand_val]
    del array[rand_val]
    less = [i for i in array if i <= num]
    greater = [i for i in array if i > num]
    return quick_sort(less) + [num] + quick_sort(greater)


def shell_sort(array):
    """
        shell sort
    :param array:
    :return:
    """
    arr_len = len(array)
    step = arr_len // 2
    while step > 0:
        for i in range(step, arr_len):
            # while i >= step and array[i] < array[i - step]:
            #     array[i], array[i - step] = array[i - step], array[i]
            #     i -= step
            for j in range(i + 1)[::-step]:
                if j >= step and array[j] < array[j - step]:
                    array[j], array[j - step] = array[j - step], array[j]
                else:
                    break
        step //= 2
    return array


def heap_sort(array):
    """
        heap sort
    :param array:
    :return:
    """
    linked_list = deque(array)

    return [linked_list[i] for i in range(1, len(linked_list))]


def merge_sort(array):
    """
        merge sort
    :param array:
    :return:
    """
    return array


def is_palindrome(x):
    """
        is palindrome
    :param x:
    :return:
    """
    if x < 0:
        return False
    if x < 10:
        return True
    # return x == int(str(x)[::-1])
    length = len(str(x))
    latter = ""
    temp = x
    half_len = length // 2
    for i in range(half_len):
        latter += str(temp % 10)
        temp = temp // 10
    if length % 2 == 0:
        # if x = 1234554321, then return x = (1234554321 // 10000)
        x = x // math.pow(10, half_len)
    else:
        # if x = 12345654321, then return x = (12345654321 // 100000)
        x = x // math.pow(10, half_len + 1)
    return str(int(x)) == latter


def two_sum(nums, target):
    """

    :param nums: list[int]
    :param target: int
    :return: list[int]
    """
    # Solution1: time complexity is too large
    # arr_len = len(nums)
    # for i in range(arr_len):
    #     for j in range(i+1, arr_len):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    # return []

    # Solution2:
    arr_len = len(nums)
    temp = {}
    for i in range(arr_len):
        minus = target - nums[i]
        if minus not in temp:
            temp[nums[i]] = i
            continue
        return [temp[minus], i]
    return []


def is_match(text, pattern):
    # if text and pattern are both empty string, return true
    if not pattern:
        return not text

    # if text is not empty string, and the first character of pattern is the first of text or '.'
    # return true
    first_match = bool(text) and pattern[0] in {text[0], '.'}

    if len(pattern) >= 2 and pattern[1] == '*':
        return (is_match(text, pattern[2:]) or
                first_match and is_match(text[1:], pattern))
    else:
        return first_match and is_match(text[1:], pattern[1:])


def add(a: int, b: int) -> int:
    """
        implement the add function without add signal
    :param a:
    :param b:
    :return:
    """
    while b != 0:
        result = a ^ b
        carry = (a & b) << 1
        a = result
        b = carry
    return a


def find_median_sorted_arrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    merged_arr = quick_sort(nums1 + nums2)
    length = len(merged_arr)
    if length % 2 == 0:
        # 1 2 3 4
        median = 0.5 * (merged_arr[length / 2] + merged_arr[length / 2 - 1])
    else:
        # 1 2 3
        median = merged_arr[length // 2 + 1]
    return median


# learn generator by Fibonacci sequence
def fib(num=1):
    idx, first, second = 0, 0, 1
    while idx < num:
        # print(second)
        yield second
        first, second = second, first + second
        idx += 1


def yang_hui_triangle(floor=1):
    idx, root = 0, [1]
    while idx < floor:
        yield root
        temp = 0
        triangle = []
        for i in root:
            temp += i
            triangle += [temp]
            temp = i
        root = triangle + [root[-1]]
        idx += 1


def normalize(name):
    return name.capitalize()


if __name__ == '__main__':
    # amicable_pair_in_range(3000)
    # seek_amicable(3000)

    # unsort_list = random.randint(1000, size=100)
    # print(unsort_list)

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

    # start_time = nanotime.nanoseconds(nanotime.now())
    # sorted_list = shell_sort(unsort_list)
    # end_time = nanotime.nanoseconds(nanotime.now())
    # print('Shell sort Used time: %dns' % (end_time - start_time))

    # print(sorted_list)

    # print(two_sum([2, 343, 32, 21, 4332, 4], 34))

    # print(is_palindrome(123456754321))

    print([1, 2, 3, 4] + [5, 6, 7, 8])
    print([1, 2, 3, 4, 5, 6, 7][::-1])
    print([i for i in fib(10)])
    print([i for i in yang_hui_triangle(5)])
    print(list(map(normalize, ["lina", "WEliNa", "LINA"])))
    print(reduce(lambda x, y: x * 10 + y, [1, 3, 5, 7, 9]))
