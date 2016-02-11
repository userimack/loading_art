import sys
import time

def loading():
	while(True):
		sys.stdout.write("\r\\")
		time.sleep(0.5)
		sys.stdout.flush()

		sys.stdout.write("\r|")
		time.sleep(0.3)
		sys.stdout.flush()

		sys.stdout.write("\r/")
		time.sleep(0.2)
		sys.stdout.flush()

		sys.stdout.write("\r-")
		time.sleep(0.1)
		sys.stdout.flush()

if __name__ == "__main__":
	loading()