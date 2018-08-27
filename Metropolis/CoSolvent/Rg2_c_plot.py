import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 
import matplotlib

matplotlib.rcParams.update({'font.size': 20})

file = "Rg2_c.dat"
c_ges = np.loadtxt(file, unpack=True)[0]/1000
c_cos = np.loadtxt(file, unpack=True)[1]/1000
Rg2 = np.loadtxt(file, unpack=True)[2]
eps = np.loadtxt(file, unpack=True)[3]
k=int(0.0)
plt.figure(figsize=(20,10))
colors = np.array(["b","r","g","c","m","y","k"])
markers = np.array(["o","v","s","+","*","p","x"])
for e in [-0.4,-0.5,-0.6,-0.7,-0.8,-0.9]: #später ncoh die anderen e ergänzen!
    Rg2plot = np.array([])
    cplot = np.array([])
    for i in np.arange(eps.size):
        #print(N[i])
        if eps[i] == e:
            Rg2plot=np.append(Rg2plot,Rg2[i])
            cplot=np.append(cplot,c_ges[i])

    sort = np.argsort(cplot)
    Rg2plot, cplot = Rg2plot[sort], cplot[sort]

    plt.subplot(1,1,1)
    ax=plt.subplot(1,1,1)
    ax.grid()
    plt.xlabel(r"$c$")
    plt.ylabel(r"$R_g^2$",rotation=0)
    ax.yaxis.set_label_coords(-0.05,0.5)
    plt.semilogx(cplot,Rg2plot, label=r"$\epsilon={}$".format(float(e)),
             color=colors[k],marker=markers[k],basex=10,ms=10)
    plt.semilogx(cplot,Rg2plot,alpha=0.6, color=colors[k],basex=10)
    plt.title(r"Gyrationsradius der Einzelkette bei variabler Gesamt-"
              + "Konzentration $c$ \n für verschiedene Wechselwirkungsenergien"
              + r" $\epsilon$")
    plt.legend(prop={'size': 20})
    k+=1

plt.subplots_adjust(left=0.07,bottom=0.09,right=0.95)
plt.show()

