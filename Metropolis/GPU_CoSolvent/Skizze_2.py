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

matplotlib.rcParams['text.latex.preamble'] = [
    r'\usepackage{amsmath}',
    r'\usepackage{amssymb}',r"\usepackage{nicefrac}",
    r"\usepackage[utf8]{inputenc}",r"\usepackage[ngerman]{babel}"]

for i in np.arange(len(sys.argv)):
    if sys.argv[i]=="cpu":
        file = "Rg2_c_CPU.dat"
        what = "CPU"
    elif sys.argv[i] == "gpu":
        file = "Rg2_c_GPU.dat"
        what = "GPU"
file="Rg2_c_Skizze.dat"
c_ges = np.loadtxt(file, unpack=True)[0]
#c_cos = np.loadtxt(file, unpack=True)[1]
Rg2 = np.loadtxt(file, unpack=True)[1]
#eps = np.loadtxt(file, unpack=True)[3]
eps= np.arange(9)*-0.4
k=int(0.0)
F=plt.figure(figsize=(12,10))
fig=F
colors = np.array(["b","r","g","c","m","darkorange","k"])
markers = np.array(["o","v","s","+","*","p","x"])
for e in [-0.4]: 
    
    ## Vor dem Plotten Datei anlegen, wenn gewünscht:
    try:
        #print(sys.argv[1])
        if sys.argv[1]=="dat":
            data = np.transpose(np.array([cplot,Rg2plot]))
            #print(data)
            #np.savetxt("Rg2_c_E{}_GPU.dat".format(e), data, delimiter= "            ", fmt="%07.3f",
                    #   header="c                Rg2        epsilon={} ".format(e))
    except Exception:
        if k == 0:
            print("Turn on .dat/.png output by handing over argument dat/png")



    plt.subplot(1,1,1)
    ax=plt.subplot(1,1,1)
    #ax.grid()
    plt.xlabel(r'$c_{Col"osungsmittel}$',fontsize=28)
    plt.ylabel(r"$R_g^2$",fontsize=28)
    #plt.xlim(10**-3,10**0)
    #ax.yaxis.set_label_coords(-0.05,0.5)
    a=0.3
    v=0.5
    ax.plot(c_ges[:-10],a*(Rg2[:-10]-(2*c_ges[:-10]-12)*(1-np.heaviside(6,1))+0.13*np.heaviside(6,1)*(c_ges[:-10]-6))+v,lw=3,color="k")
    y=a*(Rg2[:-10]-(2*c_ges[:-10]-12)*(1-np.heaviside(6,1))+0.13*np.heaviside(6,1)*(c_ges[:-10]-6))+v
    print(c_ges[:-10])
    ax.plot(c_ges[:-10],( -0.1*c_ges[:-10]+0.6)*(1-np.heaviside(6,1)))
    ax.plot(c_ges[:-10],y+np.heaviside(-c_ges[:-10]+6,1)*(-0.1*c_ges[:-10]+0.2))
    #plt.semilogx(cplot,Rg2plot, label=r"$\epsilon={}$".format(float(e)),
    #         color=colors[k],marker=markers[k],basex=10,ms=15)
    #plt.semilogx(cplot,Rg2plot,alpha=0.6, color=colors[k],basex=10)
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='major',length=0)
    ax.tick_params(right=True, direction='in',which='both')
    ax.tick_params(left=True,right=True,bottom=True,top=True,which='minor',length=5)
 #   plt.title(r"GPU: "
  #            +  r"Gyrationsradius der Einzelkette bei variabler Gesamt-"
   #           + "Konzentration $c$ \n für verschiedene Wechselwirkungsenergien"
    #          + r" $\epsilon$")
    plt.ylim(0,1.2)
    #plt.xlim(10**-3,0.16)
    ax.tick_params(axis='x', pad=10)
    ax.tick_params(axis='y', pad=10)
    #minor_locator_x = AutoMinorLocator(2)
    #minor_locator_y = AutoMinorLocator()
    #ax.xaxis.set_minor_locator(minor_locator_x)
    #ax.yaxis.set_minor_locator(minor_locator_y)
    k+=1
labels = [item.get_text() for item in ax.get_xticklabels()]

empty_string_labels = ['']*len(labels)
#ax.set_xticklabels(empty_string_labels)
labels = [item.get_text() for item in ax.get_yticklabels()]

empty_string_labels = ['']*len(labels)
ax.set_yticklabels(empty_string_labels)
#F.legend(prop={'size': fontsize},loc="upper center",ncol=6)
#plt.yticks(plt.yticks()[0][::2])


ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.subplots_adjust(left=0.07,right=0.98,top=0.915,bottom=0.09)
xmin, xmax = ax.get_xlim() 
ymin, ymax = ax.get_ylim()
dps = fig.dpi_scale_trans.inverted()
bbox = ax.get_window_extent().transformed(dps)
width, height = bbox.width, bbox.height
 
# manual arrowhead width and length
hw = 1./20.*(ymax-ymin) 
hl = 1./20.*(xmax-xmin)
lw = 1. # axis line width
ohg = 0.3 # arrow overhang
 
# compute matching arrowhead length and width
yhw = hw/(ymax-ymin)*(xmax-xmin)* height/width 
yhl = hl/(xmax-xmin)*(ymax-ymin)* width/height
 
# draw x and y axis
ax.arrow(xmin, 0, xmax-xmin, 0., fc='k', ec='k', lw = lw, 
         head_width=hw, head_length=hl, overhang = ohg, 
         length_includes_head= True, clip_on = False) 
 
ax.arrow(xmin, ymin, 0., ymax-ymin, fc='k', ec='k', lw = lw, 
         head_width=yhw, head_length=yhl, overhang = ohg, 
         length_includes_head= True, clip_on = False) 
 
for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "png":
        plt.savefig("../../../ownCloud/SS18/BA/Vortrag/Bilder/Rg2_c_plot_Skizze.png", dpi=300)        
plt.show()

