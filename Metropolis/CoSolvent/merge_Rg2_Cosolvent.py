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
c = np.array([])
#print(files)

for File in files:
    File = "data/" + File
    # Check whether File contains Rg2 data (by checking the filename):
    if File[-7:] == "Rg2.dat":
        #print("CCC:",File[22:26])
        if File[22:23]=="0":
            c = np.append(c, 0.976562)
            #print("eps bei 0", float(File[32:35]))
            eps = np.append(eps,float(File[32:35]))
        else:
            try:
                #print(File[18:21])
                c = np.append(c,float(File[22:25]))
                #print("Eps bei dreist c:",File[27:30])
                eps = np.append(eps, float(File[27:30]))
            except:
                #print(File[18:20])
                try:
                    c = np.append(c,float(File[22:24]))
                    #print("eps bei zweist c:",File[26:29])
                    eps = np.append(eps, float(File[26:29]))
                except:
                    c = np.append(c, float(File[22:23]))
                    eps = np.append(eps, float(File[25:28]))
            
        Rg2mean = np.append(Rg2mean,np.loadtxt(File, unpack=True)[0])
c_ges = c/1000
c_cos = c_ges - 0.000976562
eps = eps /-1000

#print(Rg2mean,c,eps)
 
#save data in .dat-file:
sort = np.argsort(eps)
c_ges, eps, Rg2mean, c_cos = c_ges[sort], eps[sort], Rg2mean[sort], c_cos[sort]


data = np.transpose(np.array([c_ges,c_cos,Rg2mean,eps]))
#print(data)
np.savetxt("Rg2_c_CPU.dat", data, delimiter= "            ", fmt="%07.3f",
            header="c_gesamt       c_cosolvent            Rg2mean      epsilon ")



