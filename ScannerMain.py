#-----------------------------------------------------------------------------------------------#
#                                          PROJECT ADAM                                         #
#						  	3D SCANNER - PRINTER SCANNING MAIN CODE		  						#
#-----------------------------------------------------------------------------------------------#
#   Sam Maybury  -  FEB 2018                                                                    #
#                                                                                               #          
#	This section of code is designed to operate the scanning setup. It handles the homing,		#
#	scanning and saving of the images. 															#
#	Future work includes the addition of transformation from image to STL.						#
#-----------------------------------------------------------------------------------------------#

import RPI.GPIO as GPIO
import time
import os


GPIO.setmode (GPIO.BOARD)						# Each pin has several different names, tell which convention will be used
GPIO.setwarnings (False)						# Don't print GPIO warning messages


#-----------------------------------------------------------------------------------------------#
#											PIN SETUP											#
#-----------------------------------------------------------------------------------------------#

lasers = 29										# Pin to which lasers are connected
STEP = 31										# Pin to which STEP on driver is connected
DIR = 33										# Pin to which DIR on driver is connected
startBtn = 36									# Pin to which start button is connected
endstop = 35									# Pin to which endstop is connected
powerLED = 38									# Lights when operating
workingLED = 40									# Lights when scanning begins until processing is complete

GPIO.setup (lasers, GPIO.OUT)
GPIO.setup (STEP, GPIO.OUT)
GPIO.setup (DIR, GPIO,OUT)
GPIO.setup (startBtn, GPIO.IN)
GPIO.setup (endstop, GPIO.IN) 					# ENSTOP NORMALLY OPEN BY DEFAULT
GPIO.setup (powerLED, GPIO.OUT)
GPIO.setup (workingLED, GPIO.OUT)



#-----------------------------------------------------------------------------------------------#
#										FUNCTION SETUP    										#
#-----------------------------------------------------------------------------------------------#

DIRECTORY = "/home/pi/Desktop/ScannerDev/"		# Path files are stored in

STEPS_PER_MM = 80
SPEED = 40										# mm per s
stepRate = 1/(SPEED*STEPS_PER_MM)

left = 1										# Used to write motor direction to driver
right = 0


#-----------------------------------    START BUTTON    ----------------------------------------#

btnState = False
prevBtnState = False	
startBtnPressed = False							
def checkStartButton():
	btnState = GPIO.input (startBtn)
    #if the last reading was low and this one high, print
    if (prevBtnState == False and btnState == True):		# Button is pressed
        startBtnPressed = True
  prevBtnState = btnState
  time.sleep(0.05)


#-----------------------------------    MOTION SETUP    ----------------------------------------#

position = 0				# Current position of laser (mm from left)
numMoves = 0
MAXTRAVEL = 315				# User-settable scanning length (mm)  [320mm - 5 for homing allowance]
RESOLUTION = 1				# Distance between photographed layers (mm)



def move (distance, int direction):
# This function allows for easy movement of the carriage in either direction
	# First calculate how many microsteps need to be taken to move set distance
	microsteps = distance*STEPS_PER_MM
	GPIO.output (DIR, direction)					# Write direction to driver
	# For loop pulses the driver STEP pin until set microstep value is reached
	for (i = 0, i <= microsteps, i++)
	    GPIO.output (STEP, HIGH)
	    #delay(stepRate)
	    GPIO.output (STEP, LOW)	


def home ():
# Homes the carriages to zero position when called
	move (4, right)
	GPIO.output (DIR, left)
	while endstop == LOW:
		GPIO.output (STEP, HIGH)
		#delay(stepRate)
		GPIO.output (STEP, LOW)
		
	position = 0
	numMoves = 0


#---------------------------------    MULTIPLE CAMERA SETUP    ---------------------------------#

# Install fswebcam on RPi:	sudo apt-get install fswebcam
# fswebcam allows for basic photography from a specified device
# ASSUMING CAMERAS 1 AND 2


def takePhoto (cam, num):
# Takes photos from either webcam in the specified way when called
	if cam == 1:
		command = "fswebcam -d /dev/video0 -r 640x480 --no-banner --png 9 " + DIRECTORY + "1img" + str(num) + ".png"
		os.system (command)
	elif cam == 2:
		command = "fswebcam -d /dev/video1 -r 640x480 --no-banner --png 9 --flip h " + DIRECTORY + "2img" + str(num) + ".png"
		os.system (command)
	else:
		print ("Error: Camera not detected")


#----------------------------------------------------------------------------------------------#

def normalOperation
# A function determining the normal operation of the scanner.
	checkStartButton()								# Check if start button has been pressed
	if startBtnPressed == True:
		GPIO.output(workingLED, HIGH)
		home()										# Home the carriage
		GPIO.output(lasers, HIGH)					# Turn on lasers
		for position in MAXTRAVEL:
			takePhoto (1, numMoves)
			takePhoto (2, numMoves)
			move (RESOLUTION, right)
			position = position + RESOLUTION
			numMoves = numMoves + 1
		GPIO.output(lasers, LOW)					# Turn lasers off
		home()										# Home back to zero
		startBtnPressed = False						# End process so may be redone


#-----------------------------------------------------------------------------------------------#
#										      MAIN						    					#
#-----------------------------------------------------------------------------------------------#


"""if __name__ == '__main__':
    print ("This is a test of the dual camera photograph setup")
    cam = input ("Enter camera number: ")
    takePhoto(cam, 1)"""


if __name__ == '__main__':
	GPIO.output(powerLED, HIGH)
	while True:										# Infinite loop
		normalOperation
    GPIO.OUTPUT(workingLED, LOW)






















