import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 
import matplotlib
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from matplotlib.colors import LogNorm
from matplotlib import colors, cm
fontsize=25
fontsize_label=28


matplotlib.rcParams.update({'font.size': fontsize})
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
colors = np.array(["b","r","g","c","m","darkorange","k"])
markers = np.array(["o","v","s","+","*","p","x"])
print(sys.argv,len(sys.argv))
print("notwendige Übergabe: 'cpu' oder 'gpu.'")
for i in np.arange(len(sys.argv)):
    if sys.argv[i]=="cpu":
        file = "Rg2_c_CPU.dat"
        what = "CPU"
        xmax = 0.16
    elif sys.argv[i] == "gpu":
        file = "Rg2_c_GPU.dat"
        what = "GPU"
        xmax = 0.16
    elif sys.argv[i] == "gpulongexp":
        file = "Rg2_c_GPU_long.dat"
        what = "GPU_long_exp"
        xmax = 1#0.6
        #change colors etc to match with other plots:
        colors = np.array(["saddlebrown","b","darkslategray","mediumvioletred","r","darkorange","k"])
        markers = np.array(["^","o","P","X","v","d","D"])
    elif sys.argv[i] == "gpulong":
        file = "Rg2_c_GPU_long.dat"
        what = "GPU_long"
        xmax = 1#0.6
        #change colors etc to match with other plots:
        colors = np.array(["b","darkslategray","mediumvioletred","r","darkorange","k"])
        markers = np.array(["o","P","X","v","d","D"])

c_ges = np.loadtxt(file, unpack=True)[0]
c_cos = np.loadtxt(file, unpack=True)[1]
Rg2 = np.loadtxt(file, unpack=True)[2]
eps = np.loadtxt(file, unpack=True)[3]
k=int(0.0)
F=plt.figure(figsize=(20,10))
if what == "GPU" or what == "CPU":
    eps_array=[-0.4,-0.5,-0.6,-0.7,-0.8,-0.9]
elif what == "GPU_long_exp":
    eps_array=[-0.35,-0.4,-0.425,-0.45,-0.5]#,-0.6,-0.7,-0.8,-0.9]
elif what == "GPU_long":
    eps_array = [-0.4,-0.425,-0.45,-0.5]
for e in eps_array: 
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
    #ax.grid()
    plt.xlabel(r"$c$",fontsize=25)
    plt.ylabel(r"$R_g^2$",fontsize=25)
    #plt.xlim(10**-3,10**0)
    ax.yaxis.set_label_coords(-0.05,0.5)
    if e==-0.35:
        plt.semilogx(cplot,Rg2plot, label=r"$\epsilon_{}={}$".format("{PC}",float(e)),
             color=colors[k%len(colors)],marker=markers[k%len(markers)],basex=10,ms=15
             ,lw=5,ls="--")
        #plt.semilogx(cplot,Rg2plot,alpha=1, color=colors[k%len(colors)],basex=10, lw=5, ls="--")
    else:
        plt.semilogx(cplot,Rg2plot, label=r"$\epsilon={}$".format(float(e)),
             color=colors[k%len(colors)],marker=markers[k%len(markers)],basex=10,ms=15)
        plt.semilogx(cplot,Rg2plot,alpha=0.6, color=colors[k%len(colors)],basex=10)
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='major',length=10)
    ax.tick_params(right=True, direction='in',which='both')
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='minor',length=5)
 #   plt.title(r"GPU: "
  #            +  r"Gyrationsradius der Einzelkette bei variabler Gesamt-"
   #           + "Konzentration $c$ \n für verschiedene Wechselwirkungsenergien"
    #          + r" $\epsilon$")
    plt.ylim(0,1100)
    plt.xlim(10**-3,xmax)
    ax.tick_params(axis='x', pad=10)
    ax.tick_params(axis='y', pad=10)
    #minor_locator_x = AutoMinorLocator(2)
    minor_locator_y = AutoMinorLocator(2)
    #ax.xaxis.set_minor_locator(minor_locator_x)
    ax.yaxis.set_minor_locator(minor_locator_y)
    k+=1

#xt = ax.get_xticks()
#xt=np.append(xt,0.5)
#
#xtl=xt.tolist()
#xtl[-1]=r"$5\cdot 10^{-1}$"
#ax.set_xticks(xt)
#ax.set_xticklabels([r"$10**-3$",r"$10**-2$",r"$10**-1$",r"$5*10^{-1}$"])
#plt.xlim(10**-3,xmax)
#ax.tick_params(axis='x', pad=10)

if what=="GPU_long_exp":
    img = plt.imread('explicit_solvent_sketch.png')
    #ax.imshow(img, aspect='auto',extent=(0.002,0.008,100,500),norm=LogNorm(vmin=0.01, vmax=1))
    #norm = colors.LogNorm(img.mean() + 0.5 * img.std(), img.max(), clip='True')
    #plt.imshow(img, cmap=cm.gray, norm=norm, origin="lower")

F.legend(prop={'size': fontsize},loc="upper center",ncol=6)
#plt.yticks(plt.yticks()[0][::2])
plt.subplots_adjust(left=0.07,right=0.98,top=0.915,bottom=0.09)
for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "png" and what=="GPU":
        plt.savefig("../../../ownCloud/SS18/BA/Vortrag/Bilder/Rg2_c_plot_GPU.png")
    elif sys.argv[i] == "png" and what=="CPU":
        plt.savefig("../../../ownCloud/SS18/BA/Vortrag/Bilder/Rg2_c_plot_CPU.png")
    elif sys.argv[i] == "png" and what=="GPU_long":
        plt.savefig("../../../ownCloud/SS18/BA/Vortrag/Bilder/Rg2_c_plot_GPU_long.png",dpi=300)
    elif sys.argv[i] == "png" and what=="GPU_long_exp":       
        plt.savefig("../../../ownCloud/SS18/BA/Vortrag/Bilder/Rg2_c_plot_GPU_long_exp.png",dpi=300)
plt.show()

