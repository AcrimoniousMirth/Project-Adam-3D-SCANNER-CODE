import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

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

if __name__ == '__main__':
    image = cv.imread('/home/pi/Desktop/ScannerDev/TestImage.png', cv.IMREAD_GRAYSCALE)
    contImage = imageToPoints(image)
    newImage = cv.drawContours(np.zeros(image.shape), contImage, -1, (255,255,255), 1)
    cv.imshow ('original', image)
    cv.imshow ('Contoured', newImage)

    while (1):
        c = cv.waitKey(5)
        if 'q' == chr(c & 255):
            break 

    cv.destroyAllWindows()
