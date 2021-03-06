import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 
import matplotlib
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import matplotlib.patches as mpatch

plt.rc('text', usetex=True)
plt.rc('font', family='Open Sans')
matplotlib.rcParams['text.latex.preamble'] = [
    r'\usepackage{amsmath}',
    r'\usepackage{amssymb}',r"\usepackage{nicefrac}"]


fontsize=30
fontsize_label=33 #Größe schon geändert, Rest noch anpassen!!


matplotlib.rcParams.update({'font.size': fontsize})

File="invsqrtn_T_theta.dat"

invsqrtn=np.loadtxt(File, unpack=True)[0]
T_theta=np.loadtxt(File, unpack=True)[1]

m, n =np.polyfit(invsqrtn,T_theta,1)
x=np.linspace(0,0.2,1000)#invsqrtn.min(),invsqrtn.max(),1000)
#print(invsqrtn,T_theta)
plt.figure(figsize=(20,10))
ax=plt.subplot(111)
ax.tick_params(left=True,right=True,bottom=True,top=True,which='major',length=10)
ax.tick_params(right=True, direction='in',which='both')    
ax.tick_params(left=True,right=True,bottom=True,top=True,which='minor',length=5)
minor_locator_x = AutoMinorLocator(5)
minor_locator_y = AutoMinorLocator(2)
ax.xaxis.set_minor_locator(minor_locator_x)
ax.yaxis.set_minor_locator(minor_locator_y)
#print(plt.xticks()[0])

plt.plot(invsqrtn,T_theta,'o',ms=15)
plt.plot(x,m*x+n,color="k",ls="--",label="Fitfunktion:"+r" $T_{\theta}=$"+
                                 "${0:.3f}$".format(m)+r"$\cdot N^{-\nicefrac{1}{2}}+$"+
                                 "${0:.3f}$".format(n))
#plt.title("Temperatur des coil-globule-\nPhasenübergangs für verschiedene Kettenlängen",
#          fontsize=18)
plt.ylim(0.9,1.7)
plt.xlim(0.0,0.2)
plt.yticks([0.9,1.1,1.3,1.5,1.7])
yt = ax.get_yticks() 
yt=np.append(yt,n)

ytl=yt.tolist()
ytl[-1]=r"$T_\theta^\infty$"
ax.set_yticks(yt)
ax.set_yticklabels(ytl)

plt.text(0.128,1.4,r"$\epsilon_\theta=\frac{\epsilon_{WL}}{T_\theta^\infty}\simeq -0.254$",
         fontsize=fontsize_label, bbox=dict(facecolor='none', edgecolor='none', pad=18), va='bottom')

plt.xticks([0,0.05,0.1,0.15,0.2])
ax.set_xticklabels(["$0$","$0.05$","$0.1$","$0.15$","$0.2$"])
plt.ylabel(r"$T_{\theta}$",fontsize=fontsize_label)
plt.xlabel(r"$N^{-\nicefrac{1}{2}}$",fontsize=fontsize_label)
plt.legend(loc='lower center',prop={'size':fontsize})
plt.subplots_adjust(left=0.06,top=0.985, right=0.98,bottom=0.1)

###EXPERIMENT###

rectangles = {r"" : mpatch.Rectangle((0.1255,1.39), 0.041,0.10,facecolor="none",edgecolor="k")}

for r in rectangles:
    ax.add_artist(rectangles[r])
    rx, ry = rectangles[r].get_xy()
    cx = rx + rectangles[r].get_width()/2.0
    cy = ry + rectangles[r].get_height()/2.0

    ax.annotate(r, (cx, cy), color='k', weight='bold',
                fontsize=fontsize_label, ha='center', va='center')
###ENDE EXPERIMENT###



for i in np.arange(len(sys.argv)):
    if sys.argv[i] == "png":
        plt.savefig("../../../ownCloud/SS18/BA/Vortrag/Bilder/cv_1_by_sqrtN_plot.png")

plt.show()

