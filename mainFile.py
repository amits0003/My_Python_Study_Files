from My_Python_Study_Files.Phase2.Day1.misc_util import func
from My_Python_Study_Files.Phase2.Day1.Date import Date
import time

if __name__ == "__main__":
    func()

    date_obj = Date()
    time.sleep(10)
    time_now, time_old = date_obj.getTime()
    print("Time at function call : {}".format(time_now))
