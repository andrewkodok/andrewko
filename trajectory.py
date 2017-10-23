from numpy import *
import matplotlib.pylab as plt
from math import *

graphs = int(input("Number of graphs: "))

for i in range (0,graphs):

    theta = int(input("Degree: "))
    rad = radians(theta)
    v = int(input("Velocity: "))

    numx = []
    numy = []

    time = ((2*v) * sin(rad)) / 9.8
    xvelocity = cos(rad) * v
    yvelocity = sin(rad) * v

    for t in arange(0.0,1000,0.01):

        height = (yvelocity * t) - ((9.8 * (t**2)) * 0.5)
        if height > 0:
            numy.append(height)
            numx.append(xvelocity * t)

    plt.plot(numx,numy)
plt.show()
