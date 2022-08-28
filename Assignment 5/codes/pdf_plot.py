#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

maxrange=60
maxlim=6.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1);


# numpy.random.uniform() method
r_1 = np.random.uniform(size=10**6)
r_2= np.random.uniform(size=10**6)
randvar = r_1+r_2

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

plt.plot(x[0:(maxrange-1)],pdf)
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$p_X(x)$')
plt.title("Probability Density Function")

plt.show()

plt.savefig('../figs/t_pdf.pdf')
plt.savefig('../figs/t_pdf.eps')

