# coding: utf-8
import numpy as np
import scipy.integrate
dx = 0.10
xi = np.arange(0, np.pi/2, dx)
xprime = (xi[1:] + xi[:-1])/2.
np.sum(np.sin(xprime*dx))
get_ipython().run_cell_magic('timeit', '', 'scipy.integrate.simps(np.sin(xi),dx=dx)\n\n')
get_ipython().run_cell_magic('timeit', '', 'np.trapz(np.sin(xi),dx=dx)\n\n')
get_ipython().run_cell_magic('timeit', '', 'xi = np.arange(0, np.pi/2, dx)\nxprime = (xi[1:] + xi[:-1]) / 2.\nnp.sum(np.sin(xprime*dx))\n\n')
