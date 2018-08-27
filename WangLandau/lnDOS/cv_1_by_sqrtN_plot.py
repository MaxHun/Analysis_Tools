import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 
import matplotlib

matplotlib.rcParams.update({'font.size': 15})

File="invsqrtn_T_theta.dat"

invsqrtn=np.loadtxt(File, unpack=True)[0]
T_theta=np.loadtxt(File, unpack=True)[1]

m, n =np.polyfit(invsqrtn,T_theta,1)
x=np.linspace(invsqrtn.min(),invsqrtn.max(),1000)
#print(invsqrtn,T_theta)
plt.figure(figsize=(8,6))
plt.plot(invsqrtn,T_theta,'o')
plt.plot(x,m*x+n,color="k",label="Fitfunktion:"+r" $T_{\theta}=$"+
                                 "${0:.3f}$".format(m)+r"$\cdot\frac{1}{\sqrt{N}}+$"+
                                 "${0:.3f}$".format(n))
plt.title("Temperatur des coil-globule-\nPhasenübergangs für verschiedene Kettenlängen",
          fontsize=18)
plt.ylim(0.9,1.55)
plt.xlim(0.025,0.2)
plt.ylabel(r"$T_{\theta}$")
plt.xlabel(r"$\frac{1}{\sqrt{N}}$")
plt.legend(loc='lower center')
plt.show()

