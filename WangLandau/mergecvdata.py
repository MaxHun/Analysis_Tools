import numpy as np
from matplotlib import pyplot as plt
import os
import re
import sys 



# produces a list of all files in directory:

files = os.listdir()

cv = np.array([])
T = np.array([])
N = np.array([])
#print(files)

for File in files:
    #File = "data/" + File
    # Check whether File contains cv data (by checking the filename):
    if File[-8:] =="CV_T.dat":
        print(File)
        try:
            #print(File[13:16])
            n = int(File[13:16])
        except:
            #print(File[18:20])
            n = int(File[13:15])
        T_array=np.loadtxt(File,unpack=True)[0]
        cv_array=np.loadtxt(File,unpack=True)[1]
        #print(E_array)
        for i in np.arange(np.size(T_array)):
            T = np.append(T,T_array[i])
            cv = np.append(cv,cv_array[i])
            N = np.append(N,n)
            

#print(E,lndos)
 
##save data in .dat-file:
sort = np.argsort(N)
N,T,cv = N[sort], T[sort], cv[sort]
#
#
data = np.transpose(np.array([N,T,cv]))

#print(data)
np.savetxt("cv_merged.dat", data, delimiter= "     ", fmt="%-1.3f",
            header="N            T      cv(T)")



