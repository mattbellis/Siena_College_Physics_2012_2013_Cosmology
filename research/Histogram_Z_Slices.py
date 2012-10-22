###################################################
###################################################
####                                           ####
####  To plot all data from Z_Slices_Code.py   ####
####  Creates a program to take in data saved  ####
####  from Z_Slices_Code and creates plots of  ####
####  the data for RA vs. DEC in slices of Z.  ####
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
from mpl_toolkits.mplot3d import Axes3D



################################################
###                                          ###
###          For loop to plot data           ###
###           for each slice of Z.           ###
###                                          ###
################################################

Zstep = .025
Zmax = .3299888463

for i in range(0,int(Zmax/Zstep)+1):

    #infile = open("/Users/Chris/Siena_College_Physics_2012_2013_Cosmology/research/Z-Array_is_greater_than_%.3f_and_less_than_%.3f.dat") % (i*Zstep,(i+1)*Zstep)
    infile_name = "/Users/Chris/Siena_College_Physics_2012_2013_Cosmology/research/Z-Array_is_greater_than_%.3f_and_less_than_%.3f.dat" % (i*Zstep,(i+1)*Zstep)
    print infile_name
    infile = open(infile_name)

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
    print "# galaxies: %d" % (ngals)

    index = np.arange(0,nentries,ncolumns)
    ra =  content[index]
    dec = content[index+1]
    z =   content[index+2]

    print "\nNumber of entries in coordinate arrays for %.3f to %.3f Z." % (i*Zstep,(i+1)*Zstep)
    print "# ra coords:  %d" % (len(ra))
    print "# dec coords: %d" % (len(dec))
    print "# z coords:   %d" % (len(z))

    ################################################
    ###                                          ###
    ###    1)  Plots histogram of the Z_Slice    ###
    ###                                          ###
    ################################################

    #Histogram for each Z-Slice
    plt.figure()
    plt.hist(z,bins=100)
    plt.title("Histogram of Zslice greater than "+str(i*Zstep)+" and less than "+str((i+1)*Zstep)+".png")
    plt.xlabel('Z-Value')
    plt.ylabel('Number of galaxies')
    plt.savefig("Histogram_of_Zslice_greater_than_"+str(i*Zstep)+"_and_less_than_"+str((i+1)*Zstep)+".png", orientation = 'portrait')
    #plt.show()


print "Plotting loop finished."
