###
###     Christopher Godfrey
###     Matthew Bellis
###     2 Point Correlation Function Code
### Desktop/Siena 2012 2013/M_Bellis Research/astro_data/wechsler_gals_100k.cat


################################################
###                                          ###
###          Import libraries, etc.          ###
###                                          ###
################################################

import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

infile_name = "/Users/Chris/Siena_College_Physics_2012_2013_Cosmology/python_examples/data0.dat"
#infile_name = "../python_examples/data0.dat"
print infile_name
infile = open(infile_name)

content = np.array(infile.read().split()).astype('float')

### Start off with the first index of the infile and measure its distance
### to each other point, repeat, ignoring already measured distances.
###

npts = len(content)
ncolumns = 2

index = np.arange(0,npts,ncolumns)
xcoord = content[index]
ycoord = content[index+1]
#print "# x-coordinates is" % (len(xcoord))
#print "# y-coordinates is" % (len(ycoord))

distanceList = []
densityList = []
##
##npts /= ncolumns
##
##for i in range(0,npts):
##    for j in range(i+1,npts):
##        #distance = infile[i] - infile[j]
##        distance = np.sqrt((xcoord[i])**2 + (ycoord[j])**2)
##        distanceList.append(distance)
##
###print distanceList
##
####plt.hist(x,bins=100,range=(0,6))
##plt.hist(distanceList,bins=40)
##plt.show()


##10x10 grid.

GridBlocks = 10;
##Find min and max values of x and y.
##MaxX = int(max(xcoord)+1)
##MaxY = int(max(ycoord))
##MinX = int(min(xcoord))
##MinY = int(min(ycoord))
##
##DeltaX = (MaxX-MinX)/GridBlocks
##DeltaY = (MaxY-MinY)/GridBlocks
##
##for i in np.arange(MinX,MaxX,DeltaX):
##    for j in np.arange(MinY,MaxY,DeltaY):
##        indexX1 = xcoord>i
##        indexX2 = xcoord<i+DeltaX
##        indexY1 = ycoord>j
##        indexY2 = ycoord<j+DeltaY
##
##        indexX = indexX1*indexX2
##        indexY = indexY1*indexY2
##
##        xslice = xcoord[indexX]
##        yslice = ycoord[indexY]
##
##        if len(xslice) == len(yslice):
##            densityList.append(len(xslice))
##        else:
##            print "ERROR: X amount is not equal to Y amount!"
##            print xslice
##            print yslice
##
##plt.hist(densityList)
##plt.show()

for i in np.arange(0,10,1):
    for j in np.arange(0,10,1):
    
        indexX1 = xcoord>i
        indexX2 = xcoord<i+1
        indexY1 = ycoord>j
        indexY2 = ycoord<j+1

        indexX = indexX1*indexX2
        indexY = indexY1*indexY2

        xslice = xcoord[indexX]
        yslice = ycoord[indexY]

        if len(xslice) == len(yslice):
            densityList.append(len(xslice))
        else:
            print "ERROR: X amount is not equal to Y amount!"
            print xslice
            print yslice

plt.hist(densityList)
plt.show()












