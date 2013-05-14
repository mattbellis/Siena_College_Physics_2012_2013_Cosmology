###################################################
###################################################
####                                           ####
####  To convert our current RA & DEC Coords   ####
####  into degrees and also into arcseconds.   ####
####    They are then written to their own     ####
####        separate, respectful files.        ####
####                                           ####
###################################################
###################################################



################################################
###                                          ###
###          Import libraries, etc.          ###
###                                          ###
################################################

import numpy as np
import matplotlib.pyplot as plt
import sys
from mpl_toolkits.mplot3d import Axes3D


     
infile_name = sys.argv[1] #control files in through command line
outfile_name = infile_name.split(".dat")[0]+"_cartesian.dat"

print infile_name
print outfile_name
#exit()
infile = open(infile_name)
outfile = open(outfile_name,"w+")


################################################
###                                          ###
###  1)    Splits file into 3 arrays.        ###
###  2)      How big is this array?          ###
###  3) How many galazies are in this file?  ###
###  4)      Columns are RA, Dec, and Z      ###
###  5) Make an array that has the index of  ###
###     each value we want to extract        ###
###  6) Make sure each array has same size.  ###
###                                          ###
################################################

content = np.array(infile.read().split()).astype('float')

nentries = len(content)
ncolumns = 3
ngals = nentries/ncolumns

index = np.arange(0,nentries,ncolumns)
ra =  content[index]
dec = content[index+1]
#zredshift =   content[index+2]
zredshift = 0.025*np.random.random(ngals) + 0.025

print "# galaxies: %d" % (ngals)
print "# ra coords:  %d" % (len(ra))
print "# dec coords: %d" % (len(dec))
print "# z coords:   %d" % (len(zredshift))

################################################
###                                          ###
###         Conversion of the data.          ###
###                                          ###
################################################

zredshift *= 100000.0

x = zredshift*np.cos(np.deg2rad(ra))*np.cos(np.deg2rad(dec))
y = zredshift*np.sin(np.deg2rad(ra))*np.cos(np.deg2rad(dec))
z = zredshift*np.sin(np.deg2rad(dec))

# Grab random numbers
index = np.arange(0,ngals-1)
np.random.shuffle(index)

print x[index]

for a,b,c,A,B,C in zip(x[index],y[index],z[index],ra[index],dec[index],zredshift[index]):
    output = "%8.2f %8.2f %8.2f %8.2f %8.2f %8.2f\n" % (a,b,c,A,B,C)
    outfile.write(output)

outfile.close()


# TO RUN
# go into command promt, cd to dir
# type in
# python RaDec_to_deg_Archsec.py [file name here i.e, flat_data_0.0......dat]




















