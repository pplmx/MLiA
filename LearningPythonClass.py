#!/usr/bin/env python
# @author  : mystic
# @date    : 2018/12/6 20:54
import logging
import os
import random
import subprocess
import time
from enum import Enum, unique
from multiprocessing import Pool, Process, Queue

logging.basicConfig(level=logging.INFO)


class Student:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Expected a string")
        self.__name = name

    @staticmethod
    def divide(x, y):
        try:
            return lambda: x / y
        except ZeroDivisionError as e:
            logging.error(e)
        finally:
            logging.info("End to divide.")


@unique
class Weekday(Enum):
    SUN = 0
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    Sat = 6


def run(name):
    print("Run child process %s (%s)" % (name, os.getpid()))


def long_time_task(name):
    print("Run task %s (%s)" % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s runs %0.2f seconds." % (name, (end - start)))


def write(queue: Queue):
    print("Process to write: %s" % os.getpid())
    for val in ["A", "B", "C"]:
        print("Put %s to queue..." % val)
        queue.put(val)
        time.sleep(random.random())


def read(queue: Queue):
    print("Process to read: %s" % os.getpid())
    while True:
        val = queue.get(True)
        print("Get %s from queue." % val)


if __name__ == "__main__":
    print("Parent process %s." % os.getpid())
    # create a child process
    p = Process(target=run, args=("test",))
    print("Child process will start.")
    # start child process
    p.start()
    p.join()
    print("Child process end.")
    print("==========================================")
    # default value is your CPU cores, mine is 4(Pool()<=>Pool(4)[On My Computer])
    p = Pool(5)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print("Waiting for all sub-processes done...")
    p.close()
    p.join()
    print("All sub-processes done.")
    print("==========================================")
    print("nslookup baidu.com")
    r = subprocess.call(["nslookup", "baidu.com"])
    print("Exit code %s" % r)
    print("==========================================")
    # create Queue
    queue_ = Queue()
    proc_w = Process(target=write, args=(queue_,))
    proc_r = Process(target=read, args=(queue_,))
    # start process to write
    proc_w.start()
    # start process to read
    proc_r.start()
    # wait for ending to proc_w
    proc_w.join()
    # proc_r is infinity loop, forced stop
    proc_r.terminate()
