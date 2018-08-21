import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 


file = "Rg2_merged.dat"
N = np.loadtxt(file, unpack=True)[0]
Rg2 = np.loadtxt(file, unpack=True)[1]
eps = np.loadtxt(file, unpack=True)[2]
k=int(0.0)
plt.figure(figsize=(20,10))
for n in [32.0,64.0,96.0,128.0,256.0]: #später ncoh die anderen N ergänzen!
    Rg2plot = np.array([])
    epsplot = np.array([])
    for i in np.arange(N.size):
        #print(N[i])
        if N[i] == n:
            Rg2plot=np.append(Rg2plot,Rg2[i])
            epsplot=np.append(epsplot,eps[i])

    sort = np.argsort(epsplot)
    Rg2plot, epsplot = Rg2plot[sort], epsplot[sort]

    plt.subplot(2,3,k+1)
    plt.xlabel(r"$\epsilon$")
    plt.ylabel(r"$R_g^2$")
    plt.plot(epsplot,Rg2plot,'.b')
    plt.plot(epsplot,Rg2plot, color="b")
    plt.title("N={}".format(int(n)))
    k+=1
plt.show()

