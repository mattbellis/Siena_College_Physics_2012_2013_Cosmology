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

# We need to give the full path to the directory. This will obviously be 
# different on your machine, so you will want to edit this by hand. 
infile = open('/home/bellis/Work/Astronomy/catalogs/Wechsler/wechsler_gals.cat')

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

# And just for the heck of it, we can dump the first 5 entries of each array.
print "\nFirst five entries in arrays."
print ra[0:5]
print dec[0:5]
print z[0:5]

print "\n"
