import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 
import matplotlib
from matplotlib.ticker import AutoMinorLocator
import glob
from scipy.optimize import curve_fit

fontsize=30
fontsize_label=33

colors = np.array(["b","r","g","c","m","darkorange","k"])
markers = np.array(["o","v","s","+","*","p","x"])
linestyles = np.array([":","-.","--","-"])
ls_dashes = np.array([[3,3,1,1],[1,1],[1,3,3,1],[2,4,2,4,2,8],[2,2,10,2],[]])

matplotlib.rcParams.update({'font.size': fontsize})
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage[utf8]{luainputenc}\usepackage[ngerman]{babel}')
plt.rc('font', family='Open Sans')

files=glob.glob("merge_n*.dat")
files.sort()
#print(files)
k=0
f, ax = plt.subplots(1,1,figsize=(20,10))

def ai(eps,Veff, fak):
    return (np.exp(fak*eps))/(Veff+np.exp(fak*eps))

def aimult(zahl,*args):
    return zahl * ai(*args)


for File in files:
    # nc herausfinden:
    nc = int(File[8:12])
    print(File,nc)
    epsplot = -np.loadtxt(File, unpack=True)[0]
    nisplot = np.loadtxt(File, unpack=True)[8]
    ax.plot(epsplot[::4],nisplot[::4],label=r"$N_c={}$".format(nc),
            color=colors[k],dashes=ls_dashes[k],
            lw=0,ls="-", marker=markers[k],ms=15)
    ax.set_xlabel(r"$-\epsilon$",fontsize=fontsize_label)
    ax.set_ylabel(r"$n_{Schale}$",fontsize=fontsize_label)
    for n in np.arange(len(sys.argv)):
        if sys.argv[n]=="dat":
            data = np.transpose(np.array([nisplot,epsplot]))
            np.savetxt("n_c_shell_eps_Nc{}.dat".format(nc), data, delimiter= "             ", fmt="%-1.8f",
                       header="<nCoS In NNShell>             epsilon")
    #try to fit the data:
    popt, pcov = curve_fit(ai, epsplot, nisplot/np.amax(nisplot))
    plt.plot(epsplot, np.amax(nisplot)*ai(epsplot, *popt), 
            #label=r"$V_{}={:.0f}$, $f={:.1f}$".format("{eff}",popt[0],popt[1]),
            label="Fit",
            color=colors[k])
    #print(popt)
    k+=1
ax.tick_params(left=True,right=True,bottom=True,top=True,which='major',length=10)
ax.tick_params(right=True, direction='in',which='both')    
ax.tick_params(left=True,right=True,bottom=True,top=True,which='minor',length=5)
minor_locator_x = AutoMinorLocator(2)
minor_locator_y = AutoMinorLocator(2)
ax.xaxis.set_minor_locator(minor_locator_x)
ax.yaxis.set_minor_locator(minor_locator_y)
#ax.set_xticklabels(["$-1$","$-0,8$","$-0.6$","$-0.4$",
#                    "$-0.2$","$0$",r"$\epsilon_\theta$"])
plt.text(3.8,700,
        r"Fitfunktion: $n_{Schale}=\max(n_{Schale})\frac{\exp(-f\cdot\epsilon)}{V_{eff}+\exp(-f\cdot\epsilon)}$",
        fontsize=fontsize_label)
minor_locator_x = AutoMinorLocator(2)
#minor_locator_y = AutoMinorLocator(2)
ax.xaxis.set_minor_locator(minor_locator_x)
#ax.yaxis.set_minor_locator(minor_locator_y)
#plt.xticks(plt.yticks()[0][::2]) # jeden zweiten Tick löschen
plt.xticks([0,2,4,6,8])
ax.set_xlim(0,8)
ax.set_ylim(0,1400)
plt.subplots_adjust(left=0.07,right=0.98,top=0.98,bottom=0.09)
ax.legend(loc='upper center', prop={'size': fontsize}, ncol=4)
for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "png":
        plt.savefig("../../ownCloud/SS18/BA/Vortrag/Bilder/AI_n_c_shell_plot_fit.png")
plt.show()

