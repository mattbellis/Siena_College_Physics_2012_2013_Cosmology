#!/usr/bin/env python

################################################################################
# This program will generate intitial conditions for an n-body simulation.
#
# It will randomly generate the mass, initial position and intitial velocity
# for the particles, using an (x,y,z) coordinate system.
# 
# The user can specify whether or not these values are generated from a flat
# distribution or a random distribution.
#
################################################################################



import sys
from math import *
import numpy as np
from optparse import OptionParser


################################################################################
# main
################################################################################
def main():

    # Parse the command line options
    myusage = "\nusage: %prog [options]"
    parser = OptionParser(usage = myusage)

    parser.add_option("-n", "--num-particles",  dest="nparticles", 
            default=2, help="Number of particles")

    # Parse the options
    (options, args) = parser.parse_args()

    nparticles = int(options.nparticles)
    ############################################################################
    ############################################################################
    #print "Right_Ascension , Declination"
    # Generate the config file
    print nparticles

    ra_range = 90.0
    dec_range = np.pi/4.0

    #for i in range(nparticles):
    i=0
    while (i<nparticles):
        output = ""
        # Generate the ra either from a flat or Gaussian distribution.
        ra = [0.0]
        dec = [0.0]

        ra[0] = ra_range*np.random.random_sample() 
        output += "%-7.4f " % (ra[0])
        dec[0] = acos(dec_range*np.random.random_sample())
        output += "%-7.4f " % (np.rad2deg(dec[0]))

        output += "%-7.4f " % (1.0)

        print output
        i+=1 
    
    

################################################################################
# Top-level script evironment
################################################################################
if __name__ == "__main__":
    main()
