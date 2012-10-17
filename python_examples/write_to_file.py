import numpy as np

x = np.random.random(100)
y = np.random.random(100)
z = np.random.random(100)

print x
print y
print z

output_file_name = "outdata_%d.dat" % (0)

output_file = open(output_file_name,'w+')

for xpt,ypt,zpt in zip(x,y,z):
    output = "%f %f %f\n" % (xpt,ypt,zpt)
    output_file.write(output)

output_file.close()
