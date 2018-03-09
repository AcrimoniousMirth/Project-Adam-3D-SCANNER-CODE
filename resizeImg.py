import cv2 as cv
import os


pathToImages = '/home/pi/Desktop/ScannerDev/TestPhotos/'

def resize():
    for img in os.listdir(pathToImages):
        # Filters out any rogue files (e.g. hidden)
        if img.endswith(".png"):
            image = cv.imread(pathToImages + img)
            height, width, c = image.shape
            
        
            resized = cv.resize(image, (480, 640)) 
            cv.imwrite(pathToImages + img, resized)
            nheight, nwidth, c = image.shape
            print (img+' was '+str(height)+'x'+str(width)+', now '+str(nheight)+'x'+str(nwidth))
        
        else: print ('File ' + img +''' not of format [x]img[y].png''')



print ('Processing images from:')
print ('    ' + pathToImages)
resize()
print ('Processed all images')






