import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
image = cv.imread('/home/pi/Desktop/ScannerDev/TestImage.png', cv.IMREAD_GRAYSCALE)
newImage = image.copy()


def imageToPoints (image):
    ret, discrImage = cv.threshold (image, 127, 255, 0)
    height, width = discrImage.shape
    
    # Add a line of white values to the top of the image.
    # This ensures that the binary outer contour works.
    # It is removed later before writing to point cloud.
    # Order is [y,x] i.e. [row, column]
    discrImage[0,:] = 255 # 1st row, and the whole x range
    
    img, vectImage, heirarchy = cv.findContours(discrImage, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    return vectImage
    
    
    
    
contImage = imageToPoints(image)
# from all the contours, extract the largest based off of the area
contour = max(contImage, key=cv.contourArea)

"""
print 'contour: ', contour
print 'contour[1]: ', contour[1]
print 'contour[1][0]: ', contour[1][0]
print 'contour[1][0][0]: ', contour[1][0][0]
print 'Length: ', len(contour)
"""
zVal = 1
length = len(contour)

allPoints = np.zeros((0,3))
print 'Shape: ', allPoints.shape
print 'Data type: ', allPoints.dtype


for i in contour:
    xVal, yVal = tuple(contour[0][0])
    """allPoints[i][0] = float(xVal)
    allPoints[i][1] = float(yVal)
    allPoints[i][2] = float(zVal)"""
    Point = np.array([float(xVal), float(yVal), float(zVal)])
    
    np.append(allPoints, Point, axis = 0)
    
    
print allPoints




