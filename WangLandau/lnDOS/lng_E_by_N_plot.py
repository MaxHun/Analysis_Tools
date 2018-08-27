import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 
import matplotlib

matplotlib.rcParams.update({'font.size': 20})

file = "lndos_merged.dat"
N = np.loadtxt(file, unpack=True)[0]
lndos = np.loadtxt(file, unpack=True)[2]
E = np.loadtxt(file, unpack=True)[1]
eps =np.loadtxt(file, unpack=True)[3]
k=int(0.0)
plt.figure(figsize=(20,10))
colors = np.array(["b","r","g","c","m","y","k"])
markers = np.array(["o","v","s","+","*","p","x"])
linestyles = np.array([":","-.","--","-"])
ls_dashes = np.array([[3,6,3,6,3,18],[1,1],[12,6,3,6,3,6],[2,4,2,4,2,8],[2,2,10,2],[]])
for n in [32.0,64.0,96.0,128.0,256.0,512.0]: #später ncoh die anderen N ergänzen!
    lndosplot = np.array([])
    Eplot = np.array([])
    for i in np.arange(N.size):
        #print(N[i])
        if N[i] == n and eps[i] == -0.4:
            lndosplot=np.append(lndosplot,lndos[i])
            Eplot=np.append(Eplot,E[i]/n)

    sort = np.argsort(Eplot)
    lndosplot, Eplot = lndosplot[sort], Eplot[sort]

    plt.subplot(1,1,1)
    ax=plt.subplot(1,1,1)
    plt.xlabel(r"$\frac{E}{N}$")
    plt.ylabel(r"$\ln(g(E))$")
    ax.yaxis.set_label_coords(-0.05,0.5)
   # plt.plot(Eplot,lndosplot, label="N={}".format(int(n)),
   #          color=colors[k],marker=markers[k])
    plt.plot(Eplot,lndosplot,alpha=1, color=colors[k],
            dashes=ls_dashes[k]
            ,label="N={}".format(int(n)),lw=3)
    plt.xlim(-2.4,0)
    plt.ylim(-260,460)
    plt.title(r"Zustandsdichten der linearen Kette für unterschiedliche"+ 
              r" Kettenlängen $N$"+
              "\nbei gleicher Wechselwirkungsenergie"+
              r" $\epsilon=-0.4$")
    plt.legend(prop={'size': 20})
    k+=1
plt.show()

