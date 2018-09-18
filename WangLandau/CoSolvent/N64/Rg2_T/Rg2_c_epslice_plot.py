import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys
import glob
import matplotlib
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from matplotlib.colors import LogNorm
from matplotlib import colors, cm
fontsize=30
fontsize_label=33


matplotlib.rcParams.update({'font.size': fontsize})
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
colors = np.array(["b","r","g","c","m","darkorange","k"])
markers = np.array(["o","v","s","+","*","p","x"])
linestyles = np.array([":","-.","--","-"])
ls_dashes = np.array([[3,3,1,1],[1,1],[1,3,3,1],[2,4,2,4,2,8],[2,2,10,2],[],[4,4,2,2],[3,1,3,1],[2,4,4,2],[5,1,5,1],[7,1,7,1],[7,3,7,3],[3,1,1,1,1,1]])
#print(files)
files = glob.glob("Rg2_c_slice_eps-*.dat")
files.sort()
eps_WL=-0.4
f, ax =plt.subplots(1,1, figsize=(20,10))
k=0
for File in files:
    cplot = np.loadtxt(File, unpack=True)[0]
    Rg2plot = np.loadtxt(File, unpack=True)[1]
    eps=float(File[-10:-4])
    color=colors[k%len(colors)]
    marker=markers[k%len(markers)]
    # Ausnahme für vorher nicht benutzte Werte:
    if (eps+0.45)**2<0.0003:
        color="mediumvioletred"
        marker="X"
        k-=1
    if (eps+0.55)**2<0.0003:
        color="dimgray"
        marker="D"
        k-=1
    ax.semilogx(cplot, Rg2plot,color=color, alpha=1, 
            #dashes=ls_dashes[k%len(ls_dashes)], 
            label=r"$\epsilon_{}={:.2f}$".format("{ME}",eps),
            lw=3, basex=10, marker=marker, ms=15)
    plt.xlabel(r"$c$",fontsize=fontsize_label)
    plt.ylabel(r"$R_g^2$",fontsize=fontsize_label)
    #plt.xlim(10**-3,10**0)
    ax.xaxis.set_label_coords(0.50,-0.05)
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='major',length=10)
    ax.tick_params(right=True, direction='in',which='both')
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='minor',length=5)
    plt.ylim(0,200)
    #plt.xlim(-1,0)
    ax.tick_params(axis='x', pad=10)
    ax.tick_params(axis='y', pad=10)
    #minor_locator_x = AutoMinorLocator(4)
    minor_locator_y = AutoMinorLocator(4)
    #ax.xaxis.set_minor_locator(minor_locator_x)
    ax.yaxis.set_minor_locator(minor_locator_y)
    
    k+=1    
for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "png":
        plt.savefig("../../../../../ownCloud/SS18/BA/Vortrag/Bilder/CNS_Rg2_c_epslice.png")
plt.yticks(plt.yticks()[0][::2]) # jeden zweiten Tick löschen
plt.subplots_adjust(left=0.07,right=0.98,top=0.835,bottom=0.08)
f.legend(prop={'size': fontsize},loc="upper center", ncol=int(len(files)/2+0.5))
plt.show()


