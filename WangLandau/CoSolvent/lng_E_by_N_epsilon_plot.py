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
f=plt.figure(figsize=(20,10))
colors = np.array(["b","r","g","c","m","y","k"])
markers = np.array(["o","v","s","+","*","p","x"])
linestyles = np.array([":","-.","--","-"])
ls_dashes = np.array([[3,6,3,6,3,18],[1,1],[12,6,3,6,3,6],[2,4,2,4,2,8],[2,2,10,2],[]])
for e in [-0.2,-0.4,-0.8]: #später ncoh -0.1 hinzufügen! Auch unten!
    lndosplot = np.array([])
    Eplot = np.array([])
    for i in np.arange(N.size):
        #print(N[i])
        if N[i] == 32 and eps[i] == e:
            lndosplot=np.append(lndosplot,lndos[i])
            Eplot=np.append(Eplot,E[i]/-32/e)

    sort = np.argsort(Eplot)
    lndosplot, Eplot = lndosplot[sort], Eplot[sort]

    plt.subplot(1,2,1)
    ax=plt.subplot(1,2,1)
    plt.xlabel(r"$\frac{E}{|\epsilon| N}$")
    plt.ylabel(r"$\ln(g(E))$")
    ax.yaxis.set_label_coords(-0.05,0.5)
   # plt.plot(Eplot,lndosplot, label="N={}".format(int(n)),
   #          color=colors[k],marker=markers[k])
    plt.plot(Eplot,lndosplot,alpha=1, color=colors[k],
            dashes=ls_dashes[k]
            ,label="$\epsilon={}$".format(float(e)),lw=3)
    plt.xlim(-6.1,0)
    plt.ylim(-60,60)
    #plt.title(r"Zustandsdichten der linearen Kette für unterschiedliche"+ 
    #          r" Wechselwirkungsenergien $\epsilon$ "+
    #          "\nbei konstanter Kettenlänge"+
    #          r" $N=32$")
    #plt.grid()
    #plt.legend(prop={'size': 20})
    k+=1

k=0

## es folgt einfach die obere Schleife nochmal, diesmal ohne Teilen durch e!
for e in [-0.2,-0.4,-0.8]: #später ncoh die -0.1 ergänzen!
    lndosplot = np.array([])
    Eplot = np.array([])
    for i in np.arange(N.size):
        #print(N[i])
        if N[i] == 32 and eps[i] == e:
            lndosplot=np.append(lndosplot,lndos[i])
            Eplot=np.append(Eplot,E[i]/32)

    sort = np.argsort(Eplot)
    lndosplot, Eplot = lndosplot[sort], Eplot[sort]

    plt.subplot(1,2,2)
    ax=plt.subplot(1,2,2)
    plt.xlabel(r"$\frac{E}{N}$")
    plt.ylabel(r"$\ln(g(E))$",)
    ax.yaxis.set_label_coords(-0.05,0.5)
   # plt.plot(Eplot,lndosplot, label="N={}".format(int(n)),
   #          color=colors[k],marker=markers[k])
    plt.plot(Eplot,lndosplot,alpha=1, color=colors[k],
            dashes=ls_dashes[k],lw=3)
    plt.xlim(-1.5,0)
    plt.ylim(-60,60)
    #plt.grid()
    #plt.legend(prop={'size': 20})
    k+=1
for i in [1,2]:
    ax = plt.subplot(1,2,i)
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='major',length=10)
    ax.tick_params(right=True, direction='in',which='both')
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='minor',length=5)
f.suptitle(r"Zustandsdichten der linearen Kette für unterschiedliche"+
           r" Wechselwirkungsenergien $\epsilon$ "+
           "\nbei konstanter Kettenlänge"+
           r" $N=32$")
f.legend(loc="center right")
plt.subplots_adjust(right=0.87,left=0.07)
plt.show()

