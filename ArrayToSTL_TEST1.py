########################################################################
#                              ArrayToSTL                              #
########################################################################
# This script is designed to take a given array (allPoints) and 
# convert it to an STL file


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os

from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull  

# Import the array-creation functions
from ImagesToArray import *




if __name__ == '__main__':
# For testing purposes
    pathToImages = DIRECTORY + 'TestPhotos/'
    
    print ('Extracting points from images...')
    filteredPoints = getPoints(pathToImages)
    
    #print np.array(filteredPoints)



    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    points= np.array(filteredPoints)

    hull = ConvexHull(points)

    edges = list(zip(*points))

    # Simplices define the 3 points making up a triangle
    for simplex in hull.simplices:
        plt.plot(points[simplex,0], points[simplex,1], points[simplex,2], 'r-')

    ax.plot(edges[0],edges[1],edges[2],'bo') 

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.show()


























