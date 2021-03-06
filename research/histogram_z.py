################################################################################
# This is a very fast way of reading in a text file, when
# you know how the data is formatted, e.g. how many columns
# there are.
# 
# Depending on the size of the file, this still may take some time (~5-20 sec),
# but is still faster than other traditional ways of reading in files.
#
# The trade-off is that this method works best when you have a good amount of 
# memory (RAM) available.
################################################################################

import numpy as np

# Pyplot is module for plotting in matplotlib library.
import matplotlib.pyplot as plt

# We need to give the full path to the directory. This will obviously be 
# different on your machine, so you will want to edit this by hand. 
infile = open('/Users/Chris/Desktop/M_Bellis Research/astro_data/wechsler_gals.cat')
#infile = open('/home/bellis/Work/Astronomy/catalogs/Wechsler/wechsler_gals.cat')

# This command will take the entire file, split it into different values using
# whitespace (tab,space,end-of-line), and iterpret the entries as floats 
# (as opposed to strings, characters, or integers).
content = np.array(infile.read().split()).astype('float')

# Now we have this *huge* array. We want to pull out the values we want. 
# In this case, we know that the columns are RA, Dec, and z. 

# First, how big is this array.
nentries = len(content)

# Next, how many galaxies are in this file?
ncolumns = 3
ngals = nentries/ncolumns
print "# galaxies: %d" % (ngals)

# Now we just need to make an array that has the index of each value we
# want to extract. 
index = np.arange(0,nentries,ncolumns)
# So for three columns, this index array looks like
# [0,3,6,9,12,...,nentries-2]
# We can use this now to pull out the columns we want!
ra =  content[index]
dec = content[index+1]
z =   content[index+2]

# Let's make sure these arrays at least have the same size.
print "\nNumber of entries in coordinate arrays"
print "# ra coords:  %d" % (len(ra))
print "# dec coords: %d" % (len(dec))
print "# z coords:   %d" % (len(z))

plt.hist(z,bins=100)
plt.xlabel('Z-Value')
plt.ylabel('Number of galaxies')

### Draw plot
###plt.show()
### Label Plot
##plt.title('RA v. Dec for slices of Z')
##plt.xlabel('Right Ascension')
##plt.ylabel('Declination')
##
### Save plot file
plt.savefig('Histogram_of_all_Z_100slices.png', orientation = 'portrait')
plt.show()

