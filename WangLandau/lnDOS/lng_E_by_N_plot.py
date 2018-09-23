import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 
import matplotlib
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

fontsize=30
fontsize_label=33

matplotlib.rcParams.update({'font.size': fontsize})
plt.rc('text', usetex=True)
plt.rc('font', family='Open Sans')
matplotlib.rcParams['text.latex.preamble'] = [
    r'\usepackage{amsmath}',
    r'\usepackage{amssymb}',r"\usepackage{nicefrac}"]

file = "lndos_merged.dat"
N = np.loadtxt(file, unpack=True)[0]
lndos = np.loadtxt(file, unpack=True)[2]
E = np.loadtxt(file, unpack=True)[1]
eps =np.loadtxt(file, unpack=True)[3]
k=int(0.0)
plt.figure(figsize=(20,10))

exec(open("/home/max/Analysis_Tools/colorsetc.py").read())
#colors = np.array(["b","r","g","c","m","darkorange","k"])
#markers = np.array(["o","v","s","+","*","p","x"])
#linestyles = np.array([":","-.","--","-"])
#ls_dashes = np.array([[3,6,3,6,3,18],[1,1],[12,6,3,6,3,6],[2,4,2,4,2,8],[2,2,10,2],[]])
for n in [32.0,64.0,96.0,128.0,256.0,512.0]: 
    lndosplot = np.array([])
    Eplot = np.array([])
    for i in np.arange(N.size):
        #print(N[i])
        if N[i] == n and eps[i] == -0.4:
            lndosplot=np.append(lndosplot,lndos[i])
            Eplot=np.append(Eplot,E[i]/n)

    sort = np.argsort(Eplot)
    lndosplot, Eplot = lndosplot[sort], Eplot[sort]

    plt.subplot(1,1,1)
    ax=plt.subplot(1,1,1)
    plt.xlabel(r"$E\cdot N^{-1}$",fontsize=fontsize_label)
    plt.ylabel(r"$\ln(\nicefrac{g(E)}{g(0)})$",fontsize=fontsize_label)
    ax.yaxis.set_label_coords(-0.05,0.5)
   # plt.plot(Eplot,lndosplot, label="N={}".format(int(n)),
   #          color=colors[k],marker=markers[k])
    plt.plot(Eplot,lndosplot,alpha=1, color=colors[k]
            ,dashes=ls_dashes[k]
            ,label="N={}".format(int(n)),lw=3)
    plt.xlim(-3,0)
    plt.ylim(-200,400)

    #plt.title(r"Zustandsdichten der linearen Kette für unterschiedliche"+ 
    #          r" Kettenlängen $N$"+
    #          "\nbei gleicher Wechselwirkungsenergie"+
    #          r" $\epsilon=-0.4$")
    plt.legend(prop={'size': fontsize})
    k+=1
ax.tick_params(left=True,right=True,bottom=True,top=True,which='major',length=10)
ax.tick_params(right=True, direction='in',which='both')
ax.tick_params(left=True,right=True,bottom=True,top=True,which='minor',length=5)
minor_locator_x = AutoMinorLocator(5)
minor_locator_y = AutoMinorLocator(2)
ax.xaxis.set_minor_locator(minor_locator_x)
ax.yaxis.set_minor_locator(minor_locator_y)
#plt.yticks(plt.yticks()[0][::2]) #jeden zweiten Tick löschen
plt.subplots_adjust(left=0.07,right=0.98,top=0.98,bottom=0.09)
for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "png":
        plt.savefig("../../../ownCloud/SS18/BA/Vortrag/Bilder/lng_E_by_N_plot.png")

plt.show()

