import threading
import time

'''To implement a new thread using the threading module, you have to do the following:
	+ Define a new subclass of the Thread class
	+ Overried the __init__(self[,args]) method to add additional arguments
	+ Then, override the run(self[,args]) method to implement what the thread should do when started

'''
exitFlag = 0

class myThread(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

	def run(self):
		print("Starting {}".format(self.name))
		print_time(self.name, 5, self.counter)
		print("Exiting {}".format(self.name))

def print_time(threadName, counter, delay):
	while counter:
		if exitFlag:
			threadName.exit()
		time.sleep(delay)
		print("{}: {}".format(threadName, time.ctime(time.time())))
		counter -= 1

# Created new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# start new threads
thread1.start()
thread2.start()

print("Exiting Main Thread")