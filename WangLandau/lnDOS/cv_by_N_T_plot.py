import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 
import matplotlib
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

plt.rc('text', usetex=True)
plt.rc('font', family='Open Sans')

fontsize=25
fontsize_label=28


matplotlib.rcParams.update({'font.size': fontsize})

file = "cv_merged_WL.dat"
[N,T,cv,eps]=np.loadtxt(file, unpack=True)
#N = np.loadtxt(file, unpack=True)[0]
#cv = np.loadtxt(file, unpack=True)[2]
#T = np.loadtxt(file, unpack=True)[1]
#eps = np.loadtxt(file, unpack=True)[3]
k=int(0.0)

#plt.figure(figsize=(20,10))
f, ax = plt.subplots(1,1,figsize=(20,10))
#axarr = axarr.flatten()
colors = np.array(["b","r","g","c","m","darkorange","k"])
markers = np.array(["o","v","s","+","*","p","x"])
linestyles = np.array([":","-.","--","-"])
ls_dashes = np.array([[3,3,1,1],[1,1],[1,3,3,1],[2,4,2,4,2,8],[2,2,10,2],[]])
for n in [32.0,64.0,96.0,128.0,256.0,512.0]: #später ncoh die anderen N ergänzen!
    cvplot = np.ones(50000)
    Tplot = np.ones(50000)
    #print(N.size)
    l=0
    for i in np.arange(N.size):
        #print(N[i])
        
        if N[i] == n and eps[i]==-0.4:
            cvplot[l]=cv[i]
            Tplot[l]=T[i]
            N[l]=N[i]
            #print(l)
            l+=1
    sort = np.argsort(Tplot)
    cvplot, Tplot = cvplot[sort], Tplot[sort]
    #plt.subplot(2,3,k+1)
    for i in [3,4,5]:
        ax.set_xlabel(r"$T$",fontsize=fontsize_label)
    for i in [0,3]:
        ax.set_ylabel(r"$c_V(T)$",fontsize=fontsize_label)
        #ax.yaxis.set_label_coords(-0.07,0.5)
    #ax.yaxis.set_label_coords(-0.05,0.5)
   # plt.plot(Tplot,cvplot, label="N={}".format(int(n)),
   #          color=colors[k],marker=markers[k])
    ax.plot(Tplot,cvplot/n,alpha=1, color=colors[k],
            dashes=ls_dashes[k],label="N={}".format(int(n)),lw=3)
    ax.set_xlim(0,3)
    ax.set_ylim(0,7)
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='major',length=10)
    ax.tick_params(right=True, direction='in',which='both')
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='minor',length=5)
    minor_locator_x = AutoMinorLocator(2)
    minor_locator_y = AutoMinorLocator(2)
    ax.xaxis.set_minor_locator(minor_locator_x)
    ax.yaxis.set_minor_locator(minor_locator_y)
    k+=1
#f.suptitle(r"Wärmekapazitäten unterschiedlich langer Einzelketten,"+
#           " auf Maximum normiert\n"+
#           r"bei gleicher Wechselwirkungsenergie $\epsilon=-0.4$")
    plt.subplots_adjust(wspace=0.09, hspace=0.05, top=0.98,bottom=0.09,
                    left=0.06,right=0.875)
   # plt.ylim(0,1.1)
    #plt.yticks([0,0.2,0.4,0.6,0.8,1])#plt.yticks()[0][::2])
    plt.xticks([0,1,2,3])       #plt.xticks()[0][::2])
ax.legend(loc='center right', prop={'size': fontsize})

for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "png":
        plt.savefig("../../../ownCloud/SS18/BA/Vortrag/Bilder/cV_T_plot.png")

plt.show()

