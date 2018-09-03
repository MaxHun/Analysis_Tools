import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 
import glob


# produces a list of all files in directory:

#files = os.listdir("data/")

files = glob.glob('data/*8_Rg2.dat')
#print(files)
eps = np.zeros(len(files))
Rg2mean = np.zeros(len(files))
ErrRg2 = np.zeros(len(files))
c = np.zeros(len(files))
#print(files)
k=0
#print(File[:4])
for File in files:
    #print(File[22:27])
    c_File = float(File[22:27])       
    Rg2mean_File = np.loadtxt(File, unpack=True)[0]
    #print(File[File.find('E')+1:File.find('E')+4])
    eps_File = -float(File[File.find('E')+1:File.find('E')+4]) 
    eps[k] = eps_File
    Rg2mean[k] = Rg2mean_File
    c[k] = c_File
    k+=1
c_ges = c
c_cos = c - 0.976562


#print(Rg2mean,c,eps)
 
#save data in .dat-file:
sort = np.argsort(eps)
c_ges, eps, Rg2mean, c_cos = c_ges[sort], eps[sort], Rg2mean[sort], c_cos[sort]


data = np.transpose(np.array([c_ges,c_cos,Rg2mean,eps]))
#print(data)
np.savetxt("Rg2_c_GPU.dat", data, delimiter= "            ", fmt="%07.3f",
            header="c_gesamt       c_cosolvent            Rg2mean      epsilon ")



