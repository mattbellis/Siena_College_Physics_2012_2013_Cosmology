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
outfile_name = infile_name.split(".dat")[0]+"_arcminutes.dat"

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
z =   content[index+2]

print "# galaxies: %d" % (ngals)
print "# ra coords:  %d" % (len(ra))
print "# dec coords: %d" % (len(dec))
print "# z coords:   %d" % (len(z))



################################################
###                                          ###
###         Conversion of the data.          ###
###                                          ###
################################################

    
RAarcmin = ra*60

DECarcmin = dec*60

output = "%d\n" % (len(ra))
outfile.write(output)

for RA,DEC in zip(RAarcmin,DECarcmin):
    output = "%8.2f %8.2f\n" % (RA, DEC)
    outfile.write(output)

outfile.close()


# TO RUN
# go into command promt, cd to dir
# type in
# python RaDec_to_deg_Arcmin.py [file name here i.e, flat_data_0.0......dat]




















