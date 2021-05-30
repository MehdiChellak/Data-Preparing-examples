# -*- coding: utf-8 -*-
"""
Created on Sat May 29 12:31:47 2021

@author: ASUS
"""



import glob
import cv2
from  hashlib import md5


# -------------------------- read images, converted to gray scale, resize it  ---------------
image_list = []
t=0
for filename in glob.glob('input/*.png'): # or what ever you want
    im=cv2.imread(filename)
    im= cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im=cv2.resize(im,(round(224),round(224)))
    image_list.append(im)
    t +=1
    

# --------------------------- filtre gaussien-----------------------
list_image_filtred=[]
for image in image_list:
    list_image_filtred.append(cv2.GaussianBlur(image,(5,5),0))

print("size of list image filtres : ",len(list_image_filtred))








image_list =list_image_filtred
# -------------- remove duplicated images ------------------------------------
print("intial list : ",len(image_list))
hashes = dict()
list_image3=[]

for image in image_list:
    h = md5(image).hexdigest()
    if h not in hashes:
        hashes[h]=1
        list_image3.append(image)

print("l'image finale : ",len(list_image3))
i=0
for image in list_image3:
    cv2.imwrite("./result/"+str(i)+".png",image)
    i+=1

# ----------------------- ----------------------------------- ----------------"""