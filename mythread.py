import threading
import time
from motion import startmeasure

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        if self.threadID == 1:
            startmeasure()
            # Meature()
        else:
            pass
            # MyPlot(self.name, self.counter, 5)

        #print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

# def Meature():
#     startmeasure()

# def MyPlot():


# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1