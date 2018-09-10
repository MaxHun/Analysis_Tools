import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 
import glob


# produces a list of all files in directory:

#files = os.listdir("data/")

files = glob.glob('data/merge_RD*.dat')
print(files)
eps = np.zeros(len(files))
Rg2mean = np.zeros(len(files))
ErrRg2 = np.zeros(len(files))
c = np.zeros(len(files))
#print(files)
k=0
#print(File[:4])

savefile = "Rg2_c_GPU_long.dat"
#clear output file:
open(savefile, 'w').close()
f=open(savefile,'a')
for File in files:
    #print(File[22:27])
    c_ges_File = np.loadtxt(File,unpack=True)[0]*2**-18 # Gesamtkonzentration
                                                    # c_ges=8*n(all)/128**3=n(all)*2**-18   
    Rg2mean_File = np.loadtxt(File, unpack=True)[1]
    c_cos_File = c_ges_File - 0.000976562
    #print(File[File.find('E')+1:File.find('E')+4])
    try:
        print(File[File.find('E')+1:File.find('E')+7])
        eps_File = float(File[File.find('E')+1:File.find('E')+7])
    except Exception:
        try:
            eps_File = float(File[File.find('E')+1:File.find('E')+6])
            #print((File[File.find('E')+1:File.find('E')+7]))
        except Exception:
            eps_File = float(File[File.find('E')+1:File.find('E')+5])
    eps_File = np.ones(Rg2mean_File.size)*eps_File
    sort = np.argsort(c_ges_File)
    c_ges_File, eps_File, Rg2mean_File, c_cos_File =  c_ges_File[sort], eps_File[sort], Rg2mean_File[sort], c_cos_File[sort]


    data = np.transpose(np.array([c_ges_File,c_cos_File,Rg2mean_File,eps_File]))
    #f=open(savefile,'a')
    if k==0:
        np.savetxt(f,data, delimiter= "            ", fmt="%07.3f",
                header="c_gesamt       c_cosolvent            Rg2mean      epsilon ")
    else:
        np.savetxt(f,data, delimiter= "            ", fmt="%07.3f")
    print(eps_File[0])   
    print(data)
    k+=1

 
#save data in .dat-file:
#sort = np.argsort(eps)
#c_ges, eps, Rg2mean, c_cos = c_ges[sort], eps[sort], Rg2mean[sort], c_cos[sort]


#data = np.transpose(np.array([c_ges,c_cos,Rg2mean,eps]))
#print(data)
#np.savetxt("Rg2_c_GPU_long.dat", data, delimiter= "            ", fmt="%07.3f",
#            header="c_gesamt       c_cosolvent            Rg2mean      epsilon ")



