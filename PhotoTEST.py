import time
import os

DIRECTORY = "/home/pi/Desktop/ScannerDev/"

def takePhoto (cam, num):
	if cam == 0:
		command = "fswebcam -d /dev/video0 -r 640x480 --no-banner --png 9 " + DIRECTORY + "1img" + str(num) + ".png"
		os.system (command)
	elif cam == 1:
		command = "fswebcam -d /dev/video1 -r 640x480 --no-banner --png 9 --flip h " + DIRECTORY + "2img" + str(num) + ".png"
		os.system (command)
	else:
		print("Error: Neither camera used")


if __name__ == '__main__':
    cam = input("Enter camera number: ")
    takePhoto (cam, 1)
