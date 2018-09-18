import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 



# produces a list of all files in directory:

files = os.listdir()

lndos = np.array([])
E = np.array([])
N = np.array([])
eps = np.array([])
c = np.array([])
#print(files)

for File in files:
    #File = "data/" + File
    # Check whether File contains lndos data (by checking the filename):
    if File[-26:] =="_final_HGLnDOS_shifted.dat":
        print(File)
        try:
            #print(File[13:16])
            n = 256#int(File[13:16])
        except:
            #print(File[18:20])
            n = int(File[13:15])
        E_array=np.loadtxt(File,unpack=True)[0]
        lndos_array=np.loadtxt(File,unpack=True)[1]
        #print(E_array)
        try:
            c_File=float(File[6:9])/1000
        except Exception:
            try:
                c_File=float(File[6:8])/1000
            except Exception:
                c_File=float(File[6:7])/1000


        
        try:
            eps_File=-0.4#float(File[17:21])
        except:
            eps_File = -0.4
        for i in np.arange(np.size(E_array)):
            E = np.append(E,E_array[i])
            lndos = np.append(lndos,lndos_array[i])
            N = np.append(N,n)
            eps = np.append(eps, eps_File)
            c = np.append(c,c_File)
#print(E,lndos)
 
##save data in .dat-file:
sort = np.argsort(c)
N,E,lndos,eps,c = N[sort], E[sort], lndos[sort], eps[sort], c[sort]
#
#
data = np.transpose(np.array([N,E,lndos,eps,c]))

print(data)
np.savetxt("lndos_merged.dat", data, delimiter= "     ", fmt="%-1.3f",
                    header="N             E       lndos(E)        epsilon     c_ges")



