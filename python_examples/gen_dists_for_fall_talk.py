import numpy as np
import matplotlib.pylab as plt

# Generate npts random numbers drawn from a normal (Gaussian)
# distribution with mean=5.0 and sigma=1.0
npts = 1000
mu = 5.0
sig = 0.5

#xcenter = [2.0,8.0,2.0,8.0]
#ycenter = [2.0,2.0,8.0,8.0]

xcenter = [5.0,5.0,5.0,5.0]
ycenter = [5.0,5.0,5.0,5.0]

x = np.array([])
y = np.array([])
for xc,yc in zip(xcenter,ycenter):
    # x will be a numpy array which has particular properties.
    x = np.append(x,np.random.normal(loc=mu,scale=sig,size=npts) + xc)

    # Do the same for npts more random numbers for a y-variable
    y = np.append(y,np.random.normal(loc=mu,scale=sig,size=npts) + yc)

# Make a figure on which to place the histogram
plt.figure()

# Note that we can set the number of bins (bins) and the x-axis range
# (range) in the constructor.
plt.scatter(x,y,marker='o',s=5.0,c='blue')

#outfile0 = open('data1.dat','w+')
outfile0 = open('data0.dat','w+')
for a,b in zip(x,y):
    output = "%f %f\n" % (a,b)
    outfile0.write(output)

outfile0.close()

# Generate npts random numbers drawn from a normal (Gaussian)
# distribution with mean=5.0 and sigma=1.0
# Need to call the ``show" function to get the figure to pop up.
plt.show()
