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
#print(files)

for File in files:
    #File = "data/" + File
    # Check whether File contains lndos data (by checking the filename):
    if File[-26:] =="_final_HGLnDOS_shifted.dat":
        print(File)
        try:
            #print(File[13:16])
            n = int(File[13:16])
        except:
            #print(File[18:20])
            n = int(File[13:15])
        E_array=np.loadtxt(File,unpack=True)[0]
        lndos_array=np.loadtxt(File,unpack=True)[1]
        #print(E_array)
        for i in np.arange(np.size(E_array)):
            E = np.append(E,E_array[i])
            lndos = np.append(lndos,lndos_array[i])
            N = np.append(N,n)
            

#print(E,lndos)
 
##save data in .dat-file:
sort = np.argsort(N)
N,E,lndos = N[sort], E[sort], lndos[sort]
#
#
data = np.transpose(np.array([N,E,lndos]))

#print(data)
np.savetxt("lndos_merged.dat", data, delimiter= "     ", fmt="%-1.3f",
            header="N            E      lndos(E)")



