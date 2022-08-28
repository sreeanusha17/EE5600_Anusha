import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import random

X=[]
P_e=[]
size=25000

for i in range(size):
    X.append(random.choice([1,-1]))
X=np.array(X)                   # Equiprobable Random Numbers {1,-1}
N=np.random.normal(0, 1, size)
N=np.array(N)                   # Normal Random Numbers (0,1)

for i in  range(0,11):
    Y=pow(10,i/10)*X+N                     # 10^6 Random Numbers of Y    
    P_e0=sum(np.logical_and(Y<0,X>0))/sum(X>0)
    P_e1=sum(np.logical_and(Y>0,X<0))/sum(X<0)

    P_e.append(0.5*P_e0+0.5*P_e1)
    
plt.plot(np.arange(0,11),P_e)
plt.xlabel("A value")
plt.ylabel("P_e")
plt.savefig("../figs/5_6.png")