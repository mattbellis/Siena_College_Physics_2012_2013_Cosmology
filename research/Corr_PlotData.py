###################################################
###################################################
####                                           ####
####  To plot all data from either             ####
####  randfilelist_0.%_0.%.txt or nn_0.200.out ####
####  where those files represent completly    ####
####  random flat data Z-slices and our actual ####
####  Z-slice data after having been run       ####
####  through the Corr approximation code.     ####
####  The plots are in terms of R vs. Omega.   ####
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

#infile = open('/Users/Chris/Cosmology_Research/Corr/randfilelist_0.000_0.025.txt')
infile = open('/Users/Chris/Cosmology_Research/Corr/nn_0.025.out')

################################################
###                                          ###
###  1) Splits file into its arrays.         ###
###  2) Find the length of the array.        ###
###  4) Columns are R, Omega, sig, dd,       ###
###     dr and rr.                           ###
###                                          ###
################################################

content = np.array(infile.read().split())#.astype('float')

nentries = len(content)
ncolumns = 6
print "The number of entries in the file is "+str(nentries)+"."

index = np.arange(0,nentries,ncolumns)

R       = content[index]
Omega   = content[index+1]
sig     = content[index+2] 
dd      = content[index+3]
dr      = content[index+4]
rr      = content[index+5]

print R
print Omega







##fig = plt.figure(figsize=(8,6))
##ax = fig.add_axes([-0.6, -0.75, 1.3, 1.6], projection='polar')
###ax = fig.add_axes([-0.5, -0.75, 1.0, 1.5], projection='polar')
##
###ax.scatter(ra[index],np.cos(dec[index]) ,marker ='o',s=1,c='blue')
##
##ax.scatter(np.deg2rad(ra[index]),90.0-dec[index],marker='o',s=1,c='blue')
##ax.set_rmax(92)
##
##
###ax.set_title('RA v. Dec for slices of Z',ha='left')
###ax.text(25,25, "Ra vs. Dec",ha="right",va="top")
##ax.set_xlabel('Right Ascension')
##ax.set_ylabel('Declination')
##plotfilename = "Ra_v_Dec_2D_Z-Array_is_greater_than_%4.3f_and_less_than_%4.3f.png" % (i*Zstep,(i+1)*Zstep)
###plotfilename = "plot_of_flat_%4.3f_to_%4.3f.png" % (i*Zstep,(i+1)*Zstep)
##fig.savefig(plotfilename)
##plt.show()
##
##print "Plotting finished."














