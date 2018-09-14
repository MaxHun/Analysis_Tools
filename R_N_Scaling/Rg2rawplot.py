import numpy as np
from matplotlib import pyplot as plt
import os
import re

files = os.listdir()
#print(files)

N_Given = 500

N = np.array([])
Rg2mean = np.array([])
ErrRg2 = np.array([])

for File in files:
    if File[-7:] == "Rg2.dat":
        text=open(File,'r').read()
        #print(text)

        Nloc=re.search("Number of monomers: ",text).end()
    
        try:
            N_File=int(text[Nloc:Nloc+3])
        except:
            N_File=int(text[Nloc:Nloc+2])
        N=np.append(N,N_File)
        print(N_File)
        if N_File == N_Given: 
            Rg2 = np.loadtxt(File,skiprows=19,unpack=True)[4]

        #Rg2mean = np.append(Rg2mean,Rg2.mean())
        #ErrRg2 = np.append(ErrRg2,Rg2.std())

sort = np.argsort(N)
N = N[sort]
#N, Rg2mean, ErrRg2 = N[sort], Rg2mean[sort], ErrRg2[sort]
plt.figure()
#plt.errorbar(N,Rg2mean,yerr=ErrRg2)
plt.plot(np.arange(len(Rg2)),Rg2)
plt.title("N={}".format(N_File))
plt.axhline(Rg2.mean(),color="black")
plt.axhline(Rg2.mean()-Rg2.std(),color="red")
plt.axhline(Rg2.mean()+Rg2.std(),color="red")
plt.show()
#print(Rg2mean,N,ErrRg2)
