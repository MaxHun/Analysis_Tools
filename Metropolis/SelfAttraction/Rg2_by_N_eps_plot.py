import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 
import matplotlib
from matplotlib.ticker import AutoMinorLocator

matplotlib.rcParams.update({'font.size': 20})
plt.rc('text', usetex=True)
#plt.rc('text.latex', preamble=r'\usepackage[utf8]{luainputenc}\usepackage[ngerman]{babel}')
plt.rc('font', family='Open Sans')
file = "Rg2_merged.dat"
N = np.loadtxt(file, unpack=True)[0]
Rg2 = np.loadtxt(file, unpack=True)[1]
eps = np.loadtxt(file, unpack=True)[2]
k=int(0.0)
plt.figure(figsize=(20,10))
colors = np.array(["b","r","g","c","m","y","k"])
markers = np.array(["o","v","s","+","*","p","x"])
for n in [32.0,64.0,96.0,128.0,256.0]: #später ncoh die anderen N ergänzen!
    Rg2plot = np.array([])
    epsplot = np.array([])
    for i in np.arange(N.size):
        #print(N[i])
        if N[i] == n:
            Rg2plot=np.append(Rg2plot,Rg2[i]/n)
            epsplot=np.append(epsplot,eps[i])

    sort = np.argsort(epsplot)
    Rg2plot, epsplot = Rg2plot[sort], epsplot[sort]

    plt.subplot(1,1,1)
    ax=plt.subplot(1,1,1)
    plt.xlabel(r"$\epsilon$",fontsize=25)
    plt.ylabel(r"$\frac{R_g^2}{N}$",rotation=0,fontsize=25)
    plt.ylim(0,4)
    plt.xlim(-1,0)
    ax.yaxis.set_label_coords(-0.05,0.5)
    plt.plot(epsplot,Rg2plot, label="N={}".format(int(n)),
             color=colors[k],marker=markers[k],ms=15)
    plt.plot(epsplot,Rg2plot,alpha=0.6, color=colors[k])
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='major',length=10)
    ax.tick_params(right=True, direction='in',which='both')
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='minor',length=5)
    #plt.title(r"Verhalten des Gyrationsradius bei verschiedenen"+ 
    #          r" Kettenlängen $N$ und Wechselwirkungsenergien $\epsilon$",
    #          position=(0.5,1.01))
    plt.legend(prop={'size': 20,},loc='best')
    k+=1

eps_theta=-0.2524
plt.axvline(x=eps_theta,color="k",ls="--")
plt.xticks(list(plt.xticks()[0]) + [eps_theta])
ax.set_xticklabels(["$-1$","$-0,8$","$-0.6$","$-0.4$",
                    "$-0.2$","$0$",r"$\epsilon_\theta$"])
plt.text(-0.39,3,r"$\epsilon_\theta\simeq -0.252$")
minor_locator_x = AutoMinorLocator(2)
minor_locator_y = AutoMinorLocator(2)
ax.xaxis.set_minor_locator(minor_locator_x)
ax.yaxis.set_minor_locator(minor_locator_y)
plt.yticks(plt.yticks()[0][::2]) # jeden zweiten Tick löschen
for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "png":
        plt.savefig("../../../ownCloud/SS18/BA/Vortrag/Bilder/Rg2_by_N_eps_plot.png")
plt.show()

