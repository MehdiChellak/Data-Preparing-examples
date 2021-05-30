import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

data = pd.read_csv("anime.csv")
print(data.shape)

# calcule the nullable values
compteNull=data.isnull().sum()
print(compteNull)

# replace genre with unknown
data.genre = data.genre.fillna("Unkonwn") # affectation unknown pour les valeurs NaN
result = data[data.genre=='Unkonwn']

# replace type with mode 
type_mode = data.type.mode()[0] # prend le mode
data.type = data.type.fillna(type_mode)

# replace nan rating with the mean
rating_mode = data.rating.mean() # prendre la moyenne
data.rating = data.rating.fillna(rating_mode)


## convert str to int and replace str with 0
numbers=[]
for ep in data.episodes:
    if ep.isdigit():
         numbers.append(int(ep))
    else:
         numbers.append(int(0))
data.episodes=numbers

# remplace nan de column ration with the mean of rating
moy_rating = data.rating.mean()
data.rating=data.rating.fillna(moy_rating)

#data = pd.get_dummies(data)
X = data.members.values
Y = data.episodes.values

from sklearn.linear_model import LinearRegression as LR

reg = LR()
reg.fit(np.float64(X).reshape(-1,1),Y)  #permet d'estimser les parametres

ypred = reg.predict(np.float64(X).reshape(-1,1))
plt.figure()
plt.scatter(X,Y)
plt.plot(np.float64(X).reshape(-1,1), ypred, color='blue')
plt.show()

from sklearn.metrics import r2_score
Y_p = reg.predict(np.float64(X).reshape(-1,1))
R2 = r2_score(Y, Y_p)  #coefficient de determination
print(R2)