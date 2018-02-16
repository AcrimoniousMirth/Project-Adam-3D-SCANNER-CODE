import cv2 as cv
import numpy as np
import string
#import vector

#image = cv.imread ()          # How to read image in

THRESHVAL = 128                # Value with respect to which thresholding is done



def imageToPoints (image):
    # First use threshold operator to extract the pure laser line from any ambient light
    
    ret, discrImage = cv.threshold (image, THRESHVAL, 255, 0)

    # Add a line of white values along the top of the image.
    # This ensure that the binary outside contour generation works.
    # It is removed later before points are written to point cloud.

    




DIRECTORY = "/home/Pi/Desktop/ScannerDev/TestImage.png"

image = cv.imread(DIRECTORY, 0)

threshold = imageToPoints (image)
cv.imshow('original',image)
cv.imshow('threshold',threshold)
cv.waitKey(0)
cv.destroyAllWindows()

