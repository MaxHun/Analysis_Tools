import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 
import matplotlib

matplotlib.rcParams.update({'font.size': 20})

file = "cv_merged_WL.dat"
N = np.loadtxt(file, unpack=True)[0]
cv = np.loadtxt(file, unpack=True)[2]
T = np.loadtxt(file, unpack=True)[1]
T_theta = np.array([])
invsqrtn = np.array([])
k=int(0.0)

plt.figure(figsize=(20,10))
colors = np.array(["b","r","g","c","m","y","k"])
markers = np.array(["o","v","s","+","*","p","x"])
linestyles = np.array([":","-.","--","-"])
ls_dashes = np.array([[3,6,3,6,3,18],[1,1],[12,6,3,6,3,6],[2,4,2,4,2,8],[2,2,10,2],[]])
for n in [32.0,64.0,96.0,128.0,256.0,512.0]: #später ncoh die anderen N ergänzen!
    cvplot = np.array([])
    Tplot = np.array([])
    for i in np.arange(N.size):
        #print(N[i])
        if N[i] == n:
            cvplot=np.append(cvplot,cv[i])
            Tplot=np.append(Tplot,T[i])

    sort = np.argsort(Tplot)
    cvplot, Tplot = cvplot[sort], Tplot[sort]
    
    # find the maxima of cv:
    if n == 512:
        lb=np.where(Tplot==1.401)[0][0]
    elif n == 256:
        lb=np.where(Tplot==1.307)[0][0]
    else:
        lb=0
    #print(np.size(cvplot[lb:])) 
    cvmax= cvplot[lb:].max()
    #print("cvmax:",cvmax)
    pos_cvmax=np.where(cvplot==cvmax)[0][0]
    #print("pos_cvmax:", pos_cvmax, cvplot[pos_cvmax])
    T_theta=np.append(T_theta, Tplot[pos_cvmax])
    #print("T_theta:", Tplot[pos_cvmax])
    invsqrtn=np.append(invsqrtn, np.sqrt(n)**(-1))

data = np.transpose(np.array([invsqrtn,T_theta]))

#print(data)
np.savetxt("invsqrtn_T_theta.dat", data, delimiter= "                ", 
           fmt="%-1.3f", header="N^(-1/2)            T_theta")




