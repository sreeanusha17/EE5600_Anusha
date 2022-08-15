#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
import pandas as pd 
import numpy as np

# numpy.random.uniform() method
r = np.random.uniform(size=10**6)
v=[]
for i in r:
    a=-2*np.log(1-i)
    v.append(a)
 #print(len(v))


x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = v
#randvar = np.loadtxt('gau.dat',dtype='double')
for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
plt.plot(x.T,err)#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.title("Cumulative Distribution Function")
#plt.show()
#if using termux
plt.savefig('../figs/v_cdf.pdf')
plt.savefig('../figs/v_cdf.eps')
