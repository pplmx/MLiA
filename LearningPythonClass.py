#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 2018/12/6 20:54
from enum import Enum, unique


class Student(object):

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Expected a string')
        self.__name = name


@unique
class Weekday(Enum):
    SUN = 0
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    Sat = 6

