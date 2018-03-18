########################################################################
#                              ArrayToSTL                              #
########################################################################
# This script is designed to take a given array (allPoints) and 
# convert it to an STL file


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from stl import mesh
import os

from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull  

# Import the array-creation functions
from ImagesToArray import *

#------------------------    FUNCTIONS    -----------------------------#
def arrayToConvexHull(pointArray):
# Array to STL
    # Vertices = points in array
    # Faces are defined by the corner points, listed in simplices
    vertices = np.array(pointArray)
    hull = ConvexHull(vertices)
    faces = np.array(hull.simplices)

    stlModel = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            stlModel.vectors[i][j] = vertices[f[j],:]

    # Write the mesh to file "ScanData.stl"
    stlModel.save(DIRECTORY + 'ScanData.stl')
    print ('Saved to directory as "ScanData.stl"')


def arrayToXYZ(pointArray):
# Writes all points to local .xyz file
    # Open (and write) new file in local directory
    file = open("ScanData.xyz", "w")
    
    for point in pointArray:
        xVal, yVal, zVal = point
        file.write(str(xVal)+' '+str(yVal)+' '+str(zVal)+'\n')
        
    file.close()
    print('Saved to directory as "ScanData.xyz"')


if __name__ == '__main__':
# For testing purposes
    pathToImages = DIRECTORY + 'TestPhotos/'
    
    print ('Extracting points from images...')
    filteredPoints = getPoints(pathToImages)

    arrayToConvexHull(filteredPoints)
    arrayToXYZ(filteredPoints)
   























