##########################################################################################

                                 PROJECT ADAM SCANNER CODE

##########################################################################################

ABOUT:
    Project ADAM is the name I give to my Honours Project as it is more catchy than 
"3D Scanner-Printer Hybrid for the creation of prosthetic limbs", but that's what this is.
The physical model is under construction but the scanning code is still needing a lot of
work done. 
    Imagine, if you will, a box with sides FRONT, BACK, LEFT and RIGHT.
    If lasers on sides FRONT and BACK project a laser line through the centre of the box
a stump can be stuck down into the box, interrupting the laser line and creating a 
silhouette of laser light around the stump. If then, the lasers move along the FRONT and
BACK sides of the box and there is a camera in the LEFT and RIGHT these silhouettes can
be captured for different distances along the LEFT-RIGHT axis. 
    By then using OpenCV to extract the laser line from each image we can turn it into 
an array of X, Y points and append a Z value that's derived from the distance along the
axis (which can be read from the image name where "1img34" refers to "camera 1 image 34").
These different layers are then appended to create an array of points (a Point Cloud) and
the points can then be put through a simple tessellation to create a 3D STL.

    This STL is then used by a prosthetics technician to develop a well-fitting prosthesis
and the design is printed on the same machine.

##########################################################################################

CURRENT STATE AT UPLOAD TO GITHUB:
    As it stands the code is currently in several smaller test files.
- PhotoTest holds the main code that carries out the scanning itself
- I2LTEST1 works up to the Threshold operation
- I2LTEST4 is currently under development and works up to the extraction of the points and
           subsequent writing to new array. This is what's currently under development 
           (16.02.18)
- imgToContourDEMO just proves that the program works up to the point of readContours

I PLAN TO IMPROVE THE IN-CODE DOCUMENTATION SOON














