#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 2018/6/11 20:22


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
        j = 2 * i
        while j <= ceiling:
            sum_list[j] += i
            print("sum_list[%d] = %d" % (j, sum_list[j]))
            j += i
    # The minimum known amicable number is 220
    # So starting from 220
    for i in range(220, ceiling):
        if ceiling >= sum_list[i] > i == sum_list[sum_list[i]]:
            print("( %d, %d )" % (i, sum_list[i]))


if __name__ == '__main__':
    # amicable_pair_in_range(3000)
    seek_amicable(285)
