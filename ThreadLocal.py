#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author  : mystic
# @date    : 12/10/2018 20:49

# create global ThreadLocal variable
import threading

local_school = threading.local()


def process_student():
    # get student info on current thread
    stu = local_school.student
    print('Hello, %s ( in %s ).' % (stu, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    process_student()


if __name__ == "__main__":
    t1 = threading.Thread(target=process_thread, args=("Alice",), name="Thread-A")
    t2 = threading.Thread(target=process_thread, args=("Bob",), name="Thread-B")
    t1.start()
    t2.start()
    t1.join()
    t2.join()


