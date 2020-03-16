import threading
import time


'''Dummy function that accespts 2 arguments ie filename and encryption type and sleeps for 5 seconds in a loop while printing few lines
This is to simulate a heavy function that takes 10 seconds to complete'''

def loadContents(fileName, encryptionType):
	print("Started loading contents from file: ", fileName)
	print("Encryption Type: ", encryptionType)

	for i in range(5):
		print("Loading...")
		time.sleep(1)

	print("Finished loading contents from file: ", fileName)

th = threading.Thread(target=loadContents, args=(fileName, encryptionType))

th.start()
for i in range(5):
	print("Hi From Main function")
	time.sleep(1)