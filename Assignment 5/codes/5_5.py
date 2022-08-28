#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd 
import numpy as np

import random

X=np.loadtxt('5_1.dat')
Y=np.loadtxt('5_2.dat')
total_x1=len(X)
total_x2=len(Y)

P_e0=sum(np.logical_and(Y<0,X>0))/sum(X>0)
P_e1=sum(np.logical_and(Y>0,X<0))/sum(X<0)
print(P_e0)
print(P_e1)
#df=pd.DataFrame([X_1,X_2]).T
##df.columns=['X_1','X_2']
#print(df[df[X_1>0] & df[X_2<0]])