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

exec(open("/home/max/Analysis_Tools/colorsetc.py").read())
matplotlib.rcParams.update({'font.size': fontsize})
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
#colors = np.array(["b","r","g","c","m","darkorange","k"])
#markers = np.array(["o","v","s","+","*","p","x"])
#linestyles = np.array([":","-.","--","-"])
#ls_dashes = np.array([[3,3,1,1],[1,1],[1,3,3,1],[1,1,3,1,1,1,1,1,1,1,3,1],
#                     [2,2,10,2],[],[4,4,2,2],[3,1,3,1],[2,3,5,2],[5,1,5,1],
 #                    [7,1,7,1],[3,1,3,1,1,1],[3,1,1,1,1,1]])
#print(files)
files = glob.glob("Rg2_T*.dat")
files.sort()
eps_WL=-0.4
f, ax =plt.subplots(1,1, figsize=(20,10))
k=0
epslice=False
for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "epslice":
        epslice=True
        eps_slice=float(sys.argv[i+1])
        #print(eps_slice)
c_slice=np.zeros(len(files))
Rg2_slice=np.zeros(len(files))
for File in files:
    Tplot = np.loadtxt(File, unpack=True)[0]
    Rg2plot = np.loadtxt(File, unpack=True)[1]
    epsplot = eps_WL/Tplot
    c=float(File[-9:-4])

    ax.plot(epsplot, Rg2plot,color=colors[k%len(colors)], alpha=0.6, 
            dashes=ls_dashes[k%len(ls_dashes)], label=r"$c={}$".format(c),
            lw=3)
    plt.xlabel(r"$\epsilon_{ME}=\epsilon_{WL}\cdot T^{-1}$",fontsize=fontsize_label)
    plt.ylabel(r"$R_g^2$",fontsize=fontsize_label)
    #plt.xlim(10**-3,10**0)
    #ax.yaxis.set_label_coords(-0.05,0.5)
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='major',length=10)
    ax.tick_params(right=True, direction='in',which='both')
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='minor',length=5)
    plt.ylim(0,200)
    plt.xlim(-1,0)
    ax.tick_params(axis='x', pad=10)
    ax.tick_params(axis='y', pad=10)
    minor_locator_x = AutoMinorLocator(4)
    minor_locator_y = AutoMinorLocator(5)
    ax.xaxis.set_minor_locator(minor_locator_x)
    ax.yaxis.set_minor_locator(minor_locator_y)
    
    #### Berechnen und der slice-Daten: ####
    if epslice:    
        epsdiff=(np.ones(epsplot.size)*eps_slice-epsplot)**2
        minind=np.argmin(epsdiff)
        #plt.axvline(eps_slice,ls="--")
        #plt.axvline(epsplot[minind], ls="-.")
        c_slice[k]=c
        Rg2_slice[k]=Rg2plot[minind]
    ###################################################
    k+=1    
############ Schreibe sclice-Daten:
if epslice:
    data = np.transpose(np.array([c_slice,Rg2_slice]))
    #print(data)
    np.savetxt("Rg2_c_slice_eps{0:.3f}.dat".format(epsplot[minind]), data, 
               delimiter= "            ", fmt="%07.6f",
               header="c       Rg2")
############
plt.legend(prop={'size': fontsize},loc="lower right", ncol=2)
plt.yticks(plt.yticks()[0][::2]) # jeden zweiten Tick löschen
plt.subplots_adjust(left=0.07,right=0.98,top=0.98,bottom=0.10)
for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "png":
        plt.savefig("../../../../../ownCloud/SS18/BA/Vortrag/Bilder/CNS_Rg2_T.png")

plt.show()


