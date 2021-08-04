from datetime import datetime
import time

class Date():
    """
    Class to get the current time
    """
    def __init__(self):
        self.date = datetime.now()

    def getTime(self):
        """
        function call to print the time at whoch the class is created
        :return:  current time
        """
        print("Python class is created at {}".format(self.date))
        return datetime.now(), self.date