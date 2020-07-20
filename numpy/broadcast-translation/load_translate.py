# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
d=np.loadtxt('points_circle.dat')
v=np.array([2.1,1.1])
translated=d+v
x,y=np.split(d,2,axis=1)
plt.plot(x,y,'r-')
plt.plot(translated[:,0],translated[:,1],'b-*')
plt.show()
