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
plt.rc('font', family='serif')
for i in np.arange(len(sys.argv)):
    if sys.argv[i]=="cpu":
        file = "Rg2_c_CPU.dat"
        what = "CPU"
    elif sys.argv[i] == "gpu":
        file = "Rg2_c_GPU.dat"
        what = "GPU"
c_ges = np.loadtxt(file, unpack=True)[0]
c_cos = np.loadtxt(file, unpack=True)[1]
Rg2 = np.loadtxt(file, unpack=True)[2]
eps = np.loadtxt(file, unpack=True)[3]
k=int(0.0)
F=plt.figure(figsize=(20,10))
colors = np.array(["b","r","g","c","m","darkorange","k"])
markers = np.array(["o","v","s","+","*","p","x"])
for e in [-0.4,-0.5,-0.6,-0.7,-0.8,-0.9]: 
    Rg2plot = np.array([])
    cplot = np.array([])
    for i in np.arange(eps.size):
        #print(N[i])
        if eps[i] == e:
            Rg2plot=np.append(Rg2plot,Rg2[i])
            cplot=np.append(cplot,c_ges[i])

    sort = np.argsort(cplot)
    Rg2plot, cplot = Rg2plot[sort], cplot[sort]
    
    ## Vor dem Plotten Datei anlegen, wenn gewünscht:
    try:
        #print(sys.argv[1])
        if sys.argv[1]=="dat":
            data = np.transpose(np.array([cplot,Rg2plot]))
            #print(data)
            np.savetxt("Rg2_c_E{}_GPU.dat".format(e), data, delimiter= "            ", fmt="%07.3f",
                       header="c                Rg2        epsilon={} ".format(e))
    except Exception:
        if k == 0:
            print("Turn on .dat/.png output by handing over argument dat/png")



    plt.subplot(1,1,1)
    ax=plt.subplot(1,1,1)
    ax.grid()
    plt.xlabel(r"$c$",fontsize=25)
    plt.ylabel(r"$R_g^2$",fontsize=25)
    #plt.xlim(10**-3,10**0)
    ax.yaxis.set_label_coords(-0.05,0.5)
    plt.semilogx(cplot,Rg2plot, label=r"$\epsilon={}$".format(float(e)),
             color=colors[k],marker=markers[k],basex=10,ms=15)
    plt.semilogx(cplot,Rg2plot,alpha=0.6, color=colors[k],basex=10)
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='major',length=10)
    ax.tick_params(right=True, direction='in',which='both')
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='minor',length=5)
 #   plt.title(r"GPU: "
  #            +  r"Gyrationsradius der Einzelkette bei variabler Gesamt-"
   #           + "Konzentration $c$ \n für verschiedene Wechselwirkungsenergien"
    #          + r" $\epsilon$")
    plt.ylim(0,1100)
    plt.xlim(10**-3,0.16)
    ax.tick_params(axis='x', pad=10)
    ax.tick_params(axis='y', pad=10)
    #minor_locator_x = AutoMinorLocator(2)
    minor_locator_y = AutoMinorLocator(2)
    #ax.xaxis.set_minor_locator(minor_locator_x)
    ax.yaxis.set_minor_locator(minor_locator_y)
    k+=1

F.legend(prop={'size': fontsize},loc="upper center",ncol=6)
#plt.yticks(plt.yticks()[0][::2])
plt.subplots_adjust(left=0.07,right=0.98,top=0.915,bottom=0.09)
for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "png" and what=="GPU":
        plt.savefig("../../../ownCloud/SS18/BA/Vortrag/Bilder/Rg2_c_plot_GPU.png")
    elif sys.argv[i] == "png" and what=="CPU":
        plt.savefig("../../../ownCloud/SS18/BA/Vortrag/Bilder/Rg2_c_plot_CPU.png")
        
plt.show()

