#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd 
import numpy as np

import random

X=[]
size=10**6
for i in range(size):
    X.append(random.choice([1,-1]))
X=np.array(X)                   # Equiprobable Random Numbers {1,-1}


with open(r'5_1.dat', 'w') as fp:
    for item in X:
        # write each item on a new line
        fp.write("%d\n" % item)             #5.1
#print(X)######################################################
N=np.random.normal(0, 1, size)
N=np.array(N)                   # Normal Random Numbers (0,1)

Y=pow(10,0.5)*X+N                     # 10^6 Random Numbers of Y      

##X_inverse=(1/pow(10,0.5))*(Y-N)
with open(r'5_2.dat', 'w') as fp:
    for item in Y:
        # write each item on a new line
        fp.write("%f\n" % item)           #5.2            
#######################################################
x = np.arange(0,size)#points on the x axis
plt.scatter(x,Y)
plt.xlabel("y values")
plt.ylabel('Y(y)')
#plt.show()
plt.savefig('5_3.png')

