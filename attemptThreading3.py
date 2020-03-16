import threading
import time

'''Create a Thread with a function
	This function will print 5 lines in a loop and sleep for 1 second after'''

def threadFunc():
	for i in range(5):
		print("Thread {} Hello from new Thread".format(i))
		time.sleep(1)

# '''When called, the function will complete in around 5 seconds
# 	As our main function runs in main thread, we want to create a new thread that will execute threadFunc() in parallel to main thread'''

# # Create a Thread with a function without any arguments

# th = threading.Thread(target=threadFunc)

# '''It will create Thread class object th that can run the function provided in target argument in parallel thread, but thread has not started.'''
# th.start()

# '''th.start() will start a new thread, which will exceute the function threadFunc() in parallel to main thread.
# 	After calling start() function on thread object, control will come back to Main thread and new thread will execute in parallel to Main thread'''

# for i in range(5):
# 	print("Hello From Main Thread")
# 	time.sleep(1)

# th.join()

def main():
	print("***Create a Thread with a function without any arguments***")
	th = threading.Thread(target=threadFunc)
	th.start()

	for i in range(5):
		print("Hi from Main Thread")
		time.sleep(1)

	th.join()


if __name__ == "__main__":
	main()

