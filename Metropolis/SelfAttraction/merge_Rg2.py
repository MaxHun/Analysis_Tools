import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 



# produces a list of all files in directory:

files = os.listdir("data/")

eps = np.array([])
Rg2mean = np.array([])
ErrRg2 = np.array([])
N = np.array([])
#print(files)

for File in files:
    File = "data/" + File
    # Check whether File contains Rg2 data (by checking the filename):
    if File[-7:] == "Rg2.dat":
    #print(File)
        try:
            #print(File[18:21])
            N = np.append(N,int(File[18:21]))
        except:
            #print(File[18:20])
            N = np.append(N,int(File[18:20]))
        Rg2mean = np.append(Rg2mean,np.loadtxt(File, unpack=True)[0])
    # N = np.append(N,)
        try:
            eps = np.append(eps, float(File[43:48]))
        except:
            eps = np.append(eps, float(File[44:49]))

#print(Rg2mean,N,eps)
 
#save data in .dat-file:
sort = np.argsort(N)
N,eps, Rg2mean = N[sort], eps[sort], Rg2mean[sort]


data = np.transpose(np.array([N,Rg2mean,eps]))
np.savetxt("Rg2_merged_Metropolis.dat", data, delimiter= "     ", fmt="%-1.3f",
            header="N            Rg2mean      epsilon ")



