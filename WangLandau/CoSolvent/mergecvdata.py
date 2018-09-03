import numpy as np
from matplotlib import pyplot as plt
#import os
import re
import sys 
import glob


# get all CV files, much easier than before:
files = glob.glob('*CV_T.dat')
# doesn't work yet!!

cv = np.array([])
T = np.array([])
N = np.array([])
c = np.array([])
#print(files)
k=0
for File in files:
    #File = "data/" + File
    # Check whether File contains cv data (by checking the filename):
    if File[-8:] =="CV_T.dat":
        try:
            #print(File[13:16])
            n = int(File[1:4])
        except:
            #print(File[18:20])
            n = int(File[1:3])
        T_array=np.loadtxt(File,unpack=True)[0]
        cv_array=np.loadtxt(File,unpack=True)[1]
        if k==0:
            #print(len(files))
            T=np.zeros(len(files)*np.size(T_array))
            #print(np.size(T))
            cv=np.zeros(len(files)*np.size(cv_array))
            N=np.zeros(len(files)*np.size(cv_array))
            c=np.zeros(len(files)*np.size(cv_array))
            eps=np.zeros(len(files)*np.size(cv_array))
        try:
            eps_File=float(File[17:21])
        except:
            eps_File = -0.4
        try:
            c_File=float(File[6:9])/1000
        except Exception:
            try:
                c_File=float(File[6:8])/1000
            except Exception:
                c_File=float(File[6:7])/1000 
        print(np.size(T_array))
        for i in k*np.size(T_array)+np.arange(np.size(T_array)):
            T[i] = T_array[i-k*np.size(T_array)]
            cv[i] = cv_array[i-k*np.size(T_array)]
            N[i] = n
            c[i] = c_File
            eps[i] = eps_File
        k+=1

#print(E,lndos)
 
##save data in .dat-file:
sort = np.argsort(N)
N,T,cv,eps,c = N[sort], T[sort], cv[sort], eps[sort], c[sort]
#
#
#print(np.size(T))
data = np.transpose(np.array([N,T,cv,eps,c]))

#print(data)
np.savetxt("cv_merged.dat", data, delimiter= "     ", fmt="%-1.3f",
            header="N            T      cv(T)    epsilon      c_ges")



