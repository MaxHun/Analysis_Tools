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


matplotlib.rcParams.update({'font.size': 20})

file = "cv_merged.dat"
[N,T,cv,eps,c]=np.loadtxt(file, unpack=True)
#N = np.loadtxt(file, unpack=True)[0]
#cv = np.loadtxt(file, unpack=True)[2]
#T = np.loadtxt(file, unpack=True)[1]
#eps = np.loadtxt(file, unpack=True)[3]
k=int(0.0)

#plt.figure(figsize=(20,10))
f, axarr = plt.subplots(2,7, sharex=True, sharey=True,figsize=(20,10))
axarr = axarr.flatten()
colors = np.array(["b","r","g","c","m","y","k"])
markers = np.array(["o","v","s","+","*","p","x"])
linestyles = np.array([":","-.","--","-"])
ls_dashes = np.array([[2,2,1,1],[1,1],[12,6,3,6,3,6],[2,4,2,4,2,8],[2,2,10,2],[]])

for con in np.array([1,2,3,4,6,8,11,16,23,32,45,64,91,128])/1000:
    cvplot = np.ones(50000)
    Tplot = np.ones(50000)
    #print(N.size)
    l=0
    for i in np.arange(N.size):
        #print(N[i])
        
        if N[i] == 256 and c[i]==con:
            cvplot[l]=cv[i]
            Tplot[l]=T[i]
            N[l]=256
            c[l]=con
            #print(l)
            l+=1
    sort = np.argsort(Tplot)
    cvplot, Tplot = cvplot[sort], Tplot[sort]
    #plt.subplot(2,3,k+1)
    ax=axarr[k]
    for i in [10]:
        axarr[i].set_xlabel(r"$T$",fontsize=fontsize_label)
    for i in [0,7]:
        axarr[i].set_ylabel(r"$c_V(T)$",fontsize=fontsize_label)
        axarr[i].yaxis.set_label_coords(-0.15,0.5)
    #ax.yaxis.set_label_coords(-0.05,0.5)
   # plt.plot(Tplot,cvplot, label="N={}".format(int(n)),
   #          color=colors[k],marker=markers[k])
    ax.plot(Tplot,cvplot/cvplot.max(),alpha=1, color=colors[k%len(colors)],
            dashes=ls_dashes[k%len(ls_dashes)],label="c={}".format(float(con)),lw=3)
    ax.set_xlim(0,2)
    ax.set_ylim(0,1.1)
    plt.yticks([0.2,0.4,0.6,0.8,1])
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
plt.yticks(plt.yticks()[0][::2])
plt.xticks(plt.xticks()[0][::2])
f.legend(loc='center right', prop={'size': fontsize})

for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "png":
        plt.savefig("../../../ownCloud/SS18/BA/Vortrag/Bilder/cV_T_plot.png")

plt.show()

