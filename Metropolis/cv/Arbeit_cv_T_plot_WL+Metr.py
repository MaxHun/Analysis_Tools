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
matplotlib.rcParams['text.latex.preamble'] = [
    r'\usepackage{amsmath}',
    r'\usepackage{amssymb}',r"\usepackage{nicefrac}"]
fontsize=25
fontsize_label=28


matplotlib.rcParams.update({'font.size': fontsize})

print("Mögliche Übergaben:\n"+
        "me: Es werden zusätzlich die ME-Daten geplottet\n"+
        "png: Der Plot wird als PNG exportiert\n")

file = "cv_merged_WL.dat"
file_ME = "cv_merged_ME.dat"
[N,T,cv,eps]=np.loadtxt(file, unpack=True)
[N_ME,cv_ME,eps_ME]=np.loadtxt(file_ME, unpack=True)
#N = np.loadtxt(file, unpack=True)[0]
#cv = np.loadtxt(file, unpack=True)[2]
#T = np.loadtxt(file, unpack=True)[1]
#eps = np.loadtxt(file, unpack=True)[3]
k=int(0.0)

#plt.figure(figsize=(20,10))
f, axarr = plt.subplots(3,2, sharex=True, sharey=True,figsize=(20,20))
axarr = axarr.flatten()
colors = np.array(["b","r","g","c","m","darkorange","k"])
markers = np.array(["o","v","s","+","*","p","x"])
linestyles = np.array([":","-.","--","-"])
ls_dashes = np.array([[2,2,1,1],[1,1],[12,6,3,6,3,6],[2,4,2,4,2,8],[2,2,10,2],[]])

for n in [32.0,64.0,96.0,128.0,256.0,512.0]: 
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
    lenplot_ME = int(N_ME.size/6)
    #print(lenplot_ME)
    Tplot_ME = np.zeros(lenplot_ME)
    cvplot_ME = np.zeros(lenplot_ME)
    for i in k*lenplot_ME+np.arange(lenplot_ME):
        Tplot_ME[i-k*lenplot_ME] = -0.4/eps_ME[i]
        cvplot_ME[i-k*lenplot_ME] = cv_ME[i]
    

    sort = np.argsort(Tplot)
    cvplot, Tplot = cvplot[sort], Tplot[sort]
    sort_ME = np.argsort(Tplot_ME)
    cvplot_ME, Tplot_ME = cvplot_ME[sort_ME], Tplot_ME[sort_ME]
    
    for i in np.arange(len(sys.argv)):
        if sys.argv[i] == "dat":
            data = np.transpose(np.array([Tplot,cvplot]))
            np.savetxt("cv_T_N{}_WL.dat".format(n), data, delimiter= "     ", fmt="%-1.3f",
                       header="T            cv    epsilon=-0.4        N={}".format(n))
            data_ME = np.transpose(np.array([cvplot_ME,Tplot_ME]))
            np.savetxt("cv_T_N{}_ME.dat".format(n), data, delimiter= "     ", fmt="%-1.3f",
                       header="T            cv    epsilon=-0.4        N={}".format(n))


    #plt.subplot(2,3,k+1)
    ax=axarr[k]
    for i in [4,5]:
        axarr[i].set_xlabel(r"$T$",fontsize=fontsize_label)
    for i in [0,2,4]:
        axarr[i].set_ylabel(r"$\nicefrac{c_V(T)}{c_{V,max}}$",fontsize=fontsize_label)
        axarr[i].yaxis.set_label_coords(-0.09,0.5)
    #ax.yaxis.set_label_coords(-0.05,0.5)
   # plt.plot(Tplot,cvplot, label="N={}".format(int(n)),
   #          color=colors[k],marker=markers[k])
    WL_only=True
    for i in np.arange(len(sys.argv)):
        if sys.argv[i] == "me":
            ax.plot(Tplot_ME,cvplot_ME/cvplot.max(),color=colors[k],marker=markers[k],
                    fillstyle='none', ms=15, ls="", label="ME: $N={}$".format(int(n))) 
            WL_only=False
    ax.plot(Tplot,cvplot/cvplot.max(),alpha=1, color=colors[k],
            dashes=ls_dashes[k],label="WL: $N={}$".format(int(n)),lw=3)
    ax.set_xlim(0,3)
    ax.set_ylim(0,1.25)
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
    plt.subplots_adjust(wspace=0.035, hspace=0.03, top=0.98,bottom=0.09,
                    left=0.06,right=0.83)
    plt.yticks([0,0.2,0.4,0.6,0.8,1])  #plt.yticks()[0][::2])
    plt.xticks([0,1,2,3])  #plt.xticks()[0][::2])
    plt.ylim(0,1.1)
f.legend(loc='center right', prop={'size': fontsize})

for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "png" and WL_only==True:
        plt.savefig("../../../ownCloud/SS18/BA/Vortrag/Bilder/cV_T_plot_WL_Arbeit.png")
    elif sys.argv[i] == "png" and WL_only==False:
        plt.savefig("../../../ownCloud/SS18/BA/Vortrag/Bilder/cV_T_plot_ME+WL_Arbeit.png")
plt.show()

