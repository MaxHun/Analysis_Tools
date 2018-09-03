import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 
import matplotlib
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

fontsize=25
fontsize_label=28

matplotlib.rcParams.update({'font.size': fontsize})
plt.rc('text', usetex=True)
plt.rc('font', family='Open Sans')



file = "Rg2_c_CPU.dat"
c_ges = np.loadtxt(file, unpack=True)[0]
c_cos = np.loadtxt(file, unpack=True)[1]
Rg2 = np.loadtxt(file, unpack=True)[2]
eps = np.loadtxt(file, unpack=True)[3]
k=int(0.0)
f=plt.figure(figsize=(20,10))
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
    
    for i in np.arange(len(sys.argv)):
        if sys.argv[i]=="dat":
            data=np.transpose(np.array([cplot,Rg2plot]))
            np.savetxt("Rg2_c_E{}_CPU.dat".format(e), data, 
                    delimiter= "            ", fmt="%07.3f",
                    header="c                Rg2        epsilon={} ".format(e))



    plt.subplot(1,1,1)
    ax=plt.subplot(1,1,1)
    ax.grid()
    plt.xlabel(r"$c$",fontsize=fontsize_label)
    plt.ylabel(r"$R_g^2$",fontsize=fontsize_label)
    ax.yaxis.set_label_coords(-0.04,0.5)
    plt.semilogx(cplot,Rg2plot, label=r"$\epsilon={}$".format(float(e)),
             color=colors[k],marker=markers[k],basex=10,ms=10)
    plt.semilogx(cplot,Rg2plot,alpha=0.6, color=colors[k],basex=10)
    #plt.title(r"Gyrationsradius der Einzelkette bei variabler Gesamt-"
    #          + "Konzentration $c$ \n für verschiedene Wechselwirkungsenergien"
    #          + r" $\epsilon$")
    ax.tick_params(left=True,right=True,bottom=True,top=True,
                   which='major',length=10)
    ax.tick_params(right=True, direction='in',which='both')    
    ax.tick_params(left=True,right=True,bottom=True,top=True,
                   which='minor',length=5)
    k+=1

f.legend(prop={'size': fontsize},ncol=6,loc="upper center")
plt.ylim(0,1100)
plt.xlim(10**-3,2*10**-1)
#minor_locator_x = AutoMinorLocator(2)
minor_locator_y = AutoMinorLocator(2)
#ax.xaxis.set_minor_locator(minor_locator_x)
ax.yaxis.set_minor_locator(minor_locator_y)
plt.yticks([0,200,400,600,800,1000])
ax.tick_params(axis='y', pad=10)
ax.tick_params(axis='x', pad=10)
plt.subplots_adjust(left=0.07,bottom=0.09,right=0.98,top=0.91)
for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "png":
        plt.savefig("../../../ownCloud/SS18/BA/Vortrag/Bilder/Rg2_c_plot_CPU.png")


plt.show()

