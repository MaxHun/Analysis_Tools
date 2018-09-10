import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 
import matplotlib
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import glob
fontsize=25
fontsize_label=28

matplotlib.rcParams.update({'font.size': 25})
plt.rc('text', usetex=True)
plt.rc('font', family='Open Sans')
matplotlib.rcParams['text.latex.preamble'] = [
    r'\usepackage{amsmath}',
    r'\usepackage{amssymb}',r"\usepackage{nicefrac}"]
files = glob.glob("*HG*iteration*.dat")
print(files.sort())
#N = np.loadtxt(file, unpack=True)[0]
#lndos = np.loadtxt(file, unpack=True)[2]
#E = np.loadtxt(file, unpack=True)[1]
#eps =np.loadtxt(file, unpack=True)[3]
k=int(0.0)
plt.figure(figsize=(10,10))
colors = np.array(["b","r","g","c","m","darkorange","k"])
markers = np.array(["o","v","s","+","*","p","x"])
linestyles = np.array([":","-.","--","-"])
ls_dashes = np.array([[3,3,1,1],[1,1],[1,3,3,1],[2,4,2,4,2,8],[2,2,10,2],[],[1,1,2,1]])
print(files)
for File in files: 
    lndosplot = np.loadtxt(File, unpack=True)[1]
    Eplot = np.loadtxt(File, unpack=True)[0] 
    N=64
    it=File[43:45]
    
    plt.subplot(1,1,1)
    ax=plt.subplot(1,1,1)
    plt.xlabel(r"$\frac{E}{|\epsilon |N}$",fontsize=fontsize_label)
    plt.ylabel(r"$\ln(\nicefrac{g(E)}{g(0)})$",fontsize=fontsize_label)
    ax.yaxis.set_label_coords(-0.05,0.5)
#  # plt.plot(Eplot,lndosplot, label="N={}".format(int(n)),
   #          color=colors[k],marker=markers[k])
    if int(it) in [1,4,7,10,13,16,19]:
        plt.plot(Eplot/64/0.4,lndosplot,alpha=1, color=colors[k%len(colors)],
            dashes=ls_dashes[k%len(ls_dashes)],
            label="Iteration {}".format(int(it)),lw=3)
        k+=1
    plt.xlim(-9,0)
    plt.ylim(-200,100)
    #plt.title(r"Zustandsdichten der linearen Kette für unterschiedliche"+ 
    #          r" Kettenlängen $N$"+
    #          "\nbei gleicher Wechselwirkungsenergie"+
    #          r" $\epsilon=-0.4$")
    plt.legend(prop={'size': fontsize},loc="lower right")
    #k+=1
ax.tick_params(left=True,right=True,bottom=True,top=True,which='major',length=10)
ax.tick_params(right=True, direction='in',which='both')
ax.tick_params(left=True,right=True,bottom=True,top=True,which='minor',length=5)
minor_locator_x = AutoMinorLocator(2)
minor_locator_y = AutoMinorLocator(2)
ax.xaxis.set_minor_locator(minor_locator_x)
ax.yaxis.set_minor_locator(minor_locator_y)
plt.yticks(plt.yticks()[0][::2]) #jeden zweiten Tick löschen
plt.subplots_adjust(left=0.09,right=0.98,top=0.98,bottom=0.09)
for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "png":
        plt.savefig("../../../ownCloud/SS18/BA/Vortrag/Bilder/iterationen_lng_E_by_N_plot.png")
plt.show()

