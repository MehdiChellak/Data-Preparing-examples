# -*- coding: utf-8 -*-
"""
Created on Sat May 22 14:19:42 2021

@author: ASUS
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read -------
data = pd.read_csv("garments_worker_productivity.csv")
print("data shapset est : ",data.shape)
compteNull=data.isnull().sum()
print("les null sont :",compteNull)
info = data.info()
print(info)

# replace nan wip with the mean
wip_mean = data.wip.mean() # prendre la moyenne
data.wip = data.wip.fillna(wip_mean)
compteNull=data.isnull().sum()

print(data.isnull().sum())

#-------------------------------------------
x=data.no_of_workers.values
y=data.smv.values

# ----------------- normalisation x et y ----------------------# 
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x=sc.fit_transform(np.float64(x).reshape(-1,1))
y=sc.fit_transform(np.float64(y).reshape(-1,1))

from sklearn.linear_model import LinearRegression as LR

reg = LR()
reg.fit(np.float64(x).reshape(-1,1),y)  #permet d'estimser les parametres

ypred = reg.predict(np.float64(x).reshape(-1,1))
plt.figure()
plt.scatter(x,y)
plt.plot(np.float64(x).reshape(-1,1), ypred, color='red')
plt.show()

from sklearn.metrics import r2_score
Y_p = reg.predict(np.float64(x).reshape(-1,1))
R2 = r2_score(y, Y_p)  #coefficient de determination
print("le R2  ", R2)
p=len(np.float64(x).reshape(-1,1)[0,:])
n=len(np.float64(x).reshape(-1,1)[:,0])

r2_ajuste = 1-((n-1)/(n-1-p))*(1-R2**2)
print("le r2 ajuste",r2_ajuste)