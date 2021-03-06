import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 
import matplotlib
from matplotlib.ticker import (AutoMinorLocator,MultipleLocator, 
                               FormatStrFormatter)
import glob
from scipy.optimize import curve_fit

fontsize=30
fontsize_label=33
exec(open("/home/max/Analysis_Tools/colorsetc.py").read())
#colors = np.array(["b","r","g","c","m","darkorange","k"])
#markers = np.array(["o","v","s","+","*","p","x"])
#linestyles = np.array([":","-.","--","-"])
#ls_dashes = np.array([[3,3,1,1],[1,1],[1,3,3,1],[2,4,2,4,2,8],[2,2,10,2],[]])

matplotlib.rcParams.update({'font.size': fontsize})
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage[utf8]{luainputenc}\usepackage[ngerman]{babel}')
plt.rc('font', family='Open Sans')

files=glob.glob("merge_n*.dat")
files.sort()
#print(files)
k=0
f, ax = plt.subplots(1,1,figsize=(10,10))

def ai(eps,Veff):
    return 0.019*(np.exp(eps))/(Veff+np.exp(eps))


for File in files:
    # nc herausfinden:
    try:
        nc = int(File[8:12])
    except:
        try:
            nc = int(File[8:11])
        except:
            nc = int(File[8:10])
    epsplot = -np.loadtxt(File, unpack=True)[0]
    nisplot = np.loadtxt(File, unpack=True)[8]
    nconplot = np.loadtxt(File, unpack=True)[4] # Anzahl der Kontakte
    ax.plot(epsplot,nconplot/nisplot,label=r"$N_c={}$".format(nc),
            color=colors[k],dashes=ls_dashes[k],
            lw=4,ls="-")#, marker=markers[k],ms=15)
    ax.set_xlabel(r"$\vert\epsilon\vert$",fontsize=fontsize_label)
    ax.set_ylabel(r"$n_{Kontakte}\cdot (n_{Schale})^{-1}$",fontsize=fontsize_label)
    k+=1
    for n in np.arange(len(sys.argv)):
        if sys.argv[n]=="dat":
            data = np.transpose(np.array([nconplot/nisplot,epsplot]))
            np.savetxt("n_c_by_n_shell_Nc{}.dat".format(nc), data, delimiter= "     ", fmt="%-1.8f",
                       header="<(nContacts>/<nCoS In NNShell>            epsilon")
    #try to fit the data:
    popt, pcov = curve_fit(ai, epsplot, nisplot)
    #plt.plot(-epsplot, ai(-epsplot, *popt), label="fit")

ax.tick_params(left=True,right=True,bottom=True,top=True,which='major',length=10)
ax.tick_params(right=True, direction='in',which='both')    
ax.tick_params(left=True,right=True,bottom=True,top=True,which='minor',length=5)
minor_locator_x = AutoMinorLocator(2)
minor_locator_y = AutoMinorLocator(2)
ax.xaxis.set_minor_locator(minor_locator_x)
ax.yaxis.set_minor_locator(minor_locator_y)
#ax.set_xticklabels(["$-1$","$-0,8$","$-0.6$","$-0.4$",
#                    "$-0.2$","$0$",r"$\epsilon_\theta$"])

minor_locator_x = AutoMinorLocator(4)
minor_locator_y = AutoMinorLocator(4)
ax.xaxis.set_minor_locator(minor_locator_x)
ax.yaxis.set_minor_locator(minor_locator_y)
major_locator_x = MultipleLocator(2)
major_locator_y = MultipleLocator(0.4)
ax.xaxis.set_major_locator(major_locator_x)
ax.yaxis.set_major_locator(major_locator_y)




#plt.yticks(plt.yticks()[0][::2]) # jeden zweiten Tick löschen
#plt.xticks([0,2,4,6,8])
ax.set_xlim(0,8)
ax.set_ylim(2.6,4.1)
plt.subplots_adjust(left=0.13,right=0.98,top=0.98,bottom=0.1)
ax.legend(loc='lower right', prop={'size': fontsize})
for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "png":
        plt.savefig("../../ownCloud/SS18/BA/Vortrag/Bilder/AI_n_c_by_n_shell_plot.png")
plt.show()

