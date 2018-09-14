import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 
import matplotlib
from matplotlib.ticker import AutoMinorLocator
import glob
from scipy.optimize import curve_fit

fontsize=25
fontsize_label=28

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
    nconplot = np.loadtxt(File, unpack=True)[4]
    ax.plot(epsplot,nconplot,label=r"$N_c={}$".format(nc),
            color=colors[k],dashes=ls_dashes[k],
            lw=4,ls="-")#, marker=markers[k],ms=15)
    ax.set_xlabel(r"$-\epsilon$",fontsize=fontsize_label)
    ax.set_ylabel(r"$n_{Kontakte}$",fontsize=fontsize_label)
    k+=1
    for n in np.arange(len(sys.argv)):
        if sys.argv[n]=="dat":
            data = np.transpose(np.array([nconplot,epsplot]))
            np.savetxt("ncon_eps_Nc{}.dat".format(nc), data, delimiter= "     ", fmt="%-1.8f",
                       header="<nContacts>            epsilon")
    #try to fit the data:
    popt, pcov = curve_fit(ai, epsplot, nconplot)
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

minor_locator_x = AutoMinorLocator(2)
#minor_locator_y = AutoMinorLocator(2)
ax.xaxis.set_minor_locator(minor_locator_x)
#ax.yaxis.set_minor_locator(minor_locator_y)
#plt.yticks(plt.yticks()[0][::2]) # jeden zweiten Tick löschen
plt.xticks([0,2,4,6,8])
ax.set_xlim(0,8)
ax.set_ylim(0,4500)
plt.subplots_adjust(left=0.07,right=0.98,top=0.98,bottom=0.09)
ax.legend(loc='upper left', prop={'size': fontsize})
for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "png":
        plt.savefig("../../ownCloud/SS18/BA/Vortrag/Bilder/AI_ncon_plot.png")
plt.show()

