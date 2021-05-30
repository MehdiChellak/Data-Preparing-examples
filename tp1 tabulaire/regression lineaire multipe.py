# -*- coding: utf-8 -*-
"""
Created on Sat May 22 14:19:42 2021

@author: ASUS
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 

data = pd.read_csv("garments_worker_productivity.csv")
print(data.shape)
compteNull=data.isnull().sum()

# replace nan wip with the mean
wip_mean = data.wip.mean() # prendre la moyenne
data.wip = data.wip.fillna(wip_mean)

compteNull=data.isnull().sum()



x=data[['no_of_workers','team']] # wip sa marche
y=data.smv.values

# ----------------- normalisation x et y ----------------------# 
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x=sc.fit_transform(x)
y=sc.fit_transform(np.float64(y).reshape(-1,1))

from sklearn.linear_model import LinearRegression as LR

reg = LR()
reg.fit(x,y)  # permet d'estimser les parametres

#3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X =x[:,0]
Y = y
Z =x[:,1]
ax.scatter(X, Y, Z, c='r', marker='o')
ax.set_xlabel(' X')
ax.set_ylabel(' Y')
ax.set_zlabel(' Z')
plt.show()

from sklearn.metrics import r2_score
Y_p = reg.predict(x)
R2 = r2_score(y, Y_p)  #coefficient de determination
print("le R2 : ", R2)
p=len(x[0,:])
n=len(x[:,0])
#print(p ,n)
r2_ajuste = 1-((n-1)/(n-1-p))*(1-R2**2)
print("le R2 ajuste : ",r2_ajuste)