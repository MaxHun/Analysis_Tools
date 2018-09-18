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
matplotlib.rcParams['text.latex.preamble'] = [
    r'\usepackage{amsmath}',
    r'\newcommand*\diff{\mathop{}\!\mathrm{d}}',
    r'\newcommand*\Diff[1]{\mathop{}\!\mathrm{d^#1}}']

matplotlib.rcParams.update({'font.size': fontsize})
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
colors = np.array(["b","r","g","c","m","darkorange","k"])
markers = np.array(["o","v","s","+","*","p","x"])
linestyles = np.array([":","-.","--","-"])
ls_dashes = np.array([[3,3,1,1],[1,1],[1,3,3,1],[2,4,2,4,2,8],[2,2,10,2],[],[4,4,2,2],[3,1,3,1],[2,4,4,2],[5,1,5,1],[7,1,7,1],[7,3,7,3],[3,1,1,1,1,1]])
#print(files)
files = glob.glob("Phi_fluc_T*.dat")
files.sort()
eps_WL=-0.4
f, ax =plt.subplots(1,1, figsize=(20,10))
k=0
for File in files:
    Tplot = np.loadtxt(File, unpack=True)[0]
    phiflucplot = np.loadtxt(File, unpack=True)[1]
    epsplot = eps_WL/Tplot
    c=float(File[-9:-4])

    ax.plot(epsplot, phiflucplot,color=colors[k%len(colors)], alpha=0.6, 
            dashes=ls_dashes[k%len(ls_dashes)], label=r"$c={}$".format(c),
            lw=3)
    plt.xlabel(r"$\epsilon_{ME}=\epsilon_{WL}\cdot T^{-1}$",fontsize=fontsize_label)
    plt.ylabel(r"$-\frac{\diff\phi}{\diff T}$",fontsize=fontsize_label)
    #plt.xlim(10**-3,10**0)
    #ax.yaxis.set_label_coords(-0.05,0.5)
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='major',length=10)
    ax.tick_params(right=True, direction='in',which='both')
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='minor',length=5)
    #plt.ylim(0,1)
    plt.xlim(-1,0)
    ax.tick_params(axis='x', pad=10)
    ax.tick_params(axis='y', pad=10)
    minor_locator_x = AutoMinorLocator(5)
    minor_locator_y = AutoMinorLocator(5)
    ax.xaxis.set_minor_locator(minor_locator_x)
    ax.yaxis.set_minor_locator(minor_locator_y)
    
    k+=1    

for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "png":
        plt.savefig("../../../../../ownCloud/SS18/BA/Vortrag/Bilder/CNS_phi_fluc_T.png")
#plt.xticks(plt.xticks()[0][::2]) # jeden zweiten Tick löschen
plt.subplots_adjust(left=0.07,right=0.835,top=0.98,bottom=0.10)
f.legend(prop={'size': fontsize},loc="upper right", ncol=1)
plt.show()


