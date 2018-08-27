from __future__ import unicode_literals
import numpy as np
import os
import re
import sys 
import matplotlib
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size': 20})




file = "cv_merged.dat"
N = np.loadtxt(file, unpack=True)[0]
cv = np.loadtxt(file, unpack=True)[2]
T = np.loadtxt(file, unpack=True)[1]
k=int(0.0)

#plt.figure(figsize=(20,10))
f, axarr = plt.subplots(2,3, sharex=True, sharey=True,figsize=(25,10))
axarr = axarr.flatten()
colors = np.array(["b","r","g","c","m","y","k"])
markers = np.array(["o","v","s","+","*","p","x"])
linestyles = np.array([":","-.","--","-"])
ls_dashes = np.array([[2,2,1,1],[1,1],[12,6,3,6,3,6],[2,4,2,4,2,8],[2,2,10,2],[]])
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
    #plt.subplot(2,3,k+1)
    ax=axarr[k]
    for i in [3,4,5]:
        axarr[i].set_xlabel(r"$T$")
    for i in [0,3]:
        axarr[i].set_ylabel(r"$c_V(T)$",rotation=0)
        axarr[i].yaxis.set_label_coords(-0.2,0.5)
    #ax.yaxis.set_label_coords(-0.05,0.5)
   # plt.plot(Tplot,cvplot, label="N={}".format(int(n)),
   #          color=colors[k],marker=markers[k])
    ax.plot(Tplot,cvplot/cvplot.max(),alpha=1, color=colors[k],
            dashes=ls_dashes[k],label="N={}".format(int(n)),lw=3)
    ax.set_xlim(0,3)
    #plt.title(r"Zustandsdichten der linearen Kette für unterschiedliche"+ 
    #          r" Kettenlängen $N$")
    #ax.legend(prop={'size': 20})
    k+=1
f.suptitle(r"Wärmekapazitäten unterschiedlich langer Einzelketten,"+
           " auf Maximum normiert")
plt.subplots_adjust(wspace=0.09, hspace=0.05, top=0.92)
f.legend(loc='center right', prop={'size': 20})
plt.show()

