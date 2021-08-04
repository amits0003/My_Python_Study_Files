""" Multi thread programming """

import threading
import _thread as thread
import _threading_local
import time


def print_time(threadName, delay):
    count = 0

    while count < 5:
        time.sleep(delay)
        count = count + 1
        print("S.No ", count, "%s %s" % (threadName, time.ctime(time.time())))


# create Two threads :
try:
    thread.start_new_thread(print_time, ("Thread-1", 2,))
    thread.start_new_thread(print_time, ("Thread-2", 4,))
    threading.activeCount()
except ArithmeticError as e:
    print("Unable to Start thread")


while 1:
    pass

exit()
