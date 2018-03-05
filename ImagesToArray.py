########################################################################
#                            ImagesToArray                             #
########################################################################
# This script is designed to take a given directory and output an array
# of all the points in all the images appended with a Z axis value



import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
import os

DIRECTORY = '/home/pi/Desktop/ScannerDev/'

zVal = 0            # Third dimension of all points in image
allPoints = []      # List of all points in all images
filteredPoints = [] # List of points when duplicates removed
numMoves = 0        # FOR EXAMPLE

#---------------------    FUNCTION DEFINITIONS    ---------------------#

### Image to list conversion                                           #
def imageToPoints(image):
# Takes an image and appends to allPoints list with given z value
    ret, discrImage = cv.threshold (image, 127, 255, 0)
    height, width = discrImage.shape
    
    # Add a line of white values to the top of the image.
    # This ensures that the binary outer contour works.
    # It is removed later before writing to point cloud.
    # Order is [y,x] i.e. [row, column]
    discrImage[0,:] = 255 # 1st row, and the whole x range
    
    img, vectImage, heirarchy = cv.findContours(discrImage, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    # from all the contours, extract the largest based off of the area
    contImage = max(vectImage, key=cv.contourArea)
    
    
    # Append all dimensions of point to list of all points
    for point in contImage:
        xVal, yVal = tuple(point[0])
        """allPoints[i][0] = float(xVal)
        allPoints[i][1] = float(yVal)
        allPoints[i][2] = float(zVal)"""
        if xVal > 3:
        # Skip top line of the image (white values written previously)
            point3D = (float(xVal), float(yVal), float(zVal))
    
            allPoints.append(point3D)
    
    
    return
    
def imagesToList(pathToImages):
# Iterates through directory and processes each image into array
    for img in os.listdir(pathToImages):
        # Filters out any rogue files (e.g. hidden)
        if img.endswith(".png"):
            image = cv.imread(DIRECTORY + 'TestPhotos/' + img, cv.IMREAD_GRAYSCALE)
            #print image
            if (image == None): 
                print(DIRECTORY+'TestPhotos/'+img, "could not be read!")
                return # can't go on with an invalid image
            print ('Processing ' + img)

            camNum, imgNum = os.path.splitext(img)[0].split('img')
            # print 'Camera is ', camNum
            # print 'Image is ', imgNum
        
            # Correction of values will be different for cams 1 & 2
            if camNum == 1:
                # Correction values here
                
                zVal = imgNum*numMoves
                imageToPoints(image)
                
            
            else: #camNum == 2:
                # Correction values here
            
                zVal = imgNum*numMoves
                imageToPoints(image)
                
            
        else: print ('File ' + img +''' not of format [x]img[y].png''')
    print ('Processed all images') 


### Removal of duplicates                                              #
def theCondition(xs,ys):
    # working with squares, 2.5e-05 is 0.005*0.005 
    return sum((x-y)*(x-y) for x,y in zip(xs,ys)) > 2.5e-05

def filterPoints(checkValues,condition):
    print (str(len(checkValues)) + ' points')
    print ('Removing duplicates...')
    result = []
    i = 0
    for value in checkValues:
        i = i + 1
        print ('\rProcessing ' + str(i) + ' of ' + str(len(checkValues))),
        
        if all(condition(value,other) for other in result):
            result.append(value)
    print ('\n' + str(len(result)) + ' points remaining')
    return result


### Overall function                                                   #
def getPoints(pathToImages):
    imagesToList(pathToImages)
    return filterPoints(allPoints, theCondition)


#-----------------------------    MAIN    -----------------------------#

if __name__ == '__main__':
# For testing purposes
    pathToImages = DIRECTORY + 'TestPhotos/'
    
    print ('Extracting points from images...')
    filteredPoints = getPoints(pathToImages)
    
    print np.array(filteredPoints)
    
    
    





