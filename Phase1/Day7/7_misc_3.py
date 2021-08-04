""" Multithreading priority queue """

import queue
import threading
import time

threadList = ['Thread-1', 'Thread-2', 'Thread-3']
nameList = ['one', 'two', 'three', 'four', 'five']
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1
exitFlag = 0


def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s processing : %s " % (threadName, data), " ")
        else:
            queueLock.release()
        time.sleep(1)


class myThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def __sizeof__(self):
        print("Size of Queue : ", self.__sizeof__(self))

    def run(self):
        print("Starting : ", self.name)
        process_data(self.name, self.q)
        print("Exiting :", self.name)


# Create new Threads
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID = threadID + 1


# Fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# wait for queue to be empty

while not workQueue.empty():
    pass


# Notify threads , it's time to EXIT !!!!!!!!!!!!
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()

print("Exiting Main Thread ")


