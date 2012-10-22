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

#Zstep = .025
#Zmax = .3299888463

#for i in range(0,int(Zmax/Zstep)+1):

    #infile = open("/Users/Chris/Siena_College_Physics_2012_2013_Cosmology/research/Z-Array_is_greater_than_%.3f_and_less_than_%.3f.dat") % (i*Zstep,(i+1)*Zstep)
    #infile = open("/Users/Chris/Siena_College_Physics_2012_2013_Cosmology/research/Z-Array_is_greater_than_"+str(i*Zstep)+"_and_less_than_"+str((i+1)*Zstep)+".dat")
infile = open("/Users/Chris/Siena_College_Physics_2012_2013_Cosmology/research/Z-Array_is_greater_than_0.000_and_less_than_0.025.dat")

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

print "\nNumber of entries in coordinate arrays"
print "# ra coords:  %d" % (len(ra))
print "# dec coords: %d" % (len(dec))
print "# z coords:   %d" % (len(z))

################################################
###                                          ###
###  1)    Set up 3D plot coordinates        ###
###     in terms of radius, theta and phi.   ###
###  2) Set up a subplot for polar plotting. ###
###  3)     Assign it as a scatter plot.     ###
###                                          ###
################################################

#Choose 5k random points to plot. 
indexran = range(100000)
np.random.shuffle(indexran)
index = index[0:5000]

radius = z[index].copy()
theta = np.deg2rad(ra[index])
phi = np.deg2rad(dec[index])
x = radius*np.cos(theta)*np.cos(phi)
y = radius*np.sin(theta)*np.cos(phi)
z = radius*np.sin(phi)

plt.figure()
ax = plt.subplot(111,projection='3d')
#plt.scatter(ra[index],np.cos(np.deg2rad(dec[index])),marker='o',s=1,c='blue')
ax.scatter(x,y,z,s=1,c='b',marker='o')

plt.show()
plt.title('RA v. Dec for slices of Z')
plt.xlabel('Right Ascension')
plt.ylabel('Declination')

#plt.savefig('Ra_v_Dec_Z-Array_is_greater_than_%.3f_and_less_than_%.3f.png') % (i*Zstep,(i+1)*Zstep)
plt.savefig('Ra_v_Dec_Z-Array_is_greater_than_0.000_and_less_than_0.025.png')


#print "Plotting loop finished."
