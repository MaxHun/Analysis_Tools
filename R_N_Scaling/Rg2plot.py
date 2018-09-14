import numpy as np
from matplotlib import pyplot as plt
import os
import re
from scipy import optimize

# produces a list of all files in directory:

files = os.listdir()
#print(files)

# initializig arrays for N Rg2 an delRg2:
N = np.array([])
Rg2mean = np.array([])
ErrRg2 = np.array([])

for File in files:

    # Check whether File[i] contains Rg2 data (by cheching the filename):
    if File[-7:] == "Rg2.dat":
        text=open(File,'r').read()
        #print(text)
        
        # find number of monomers in the file:
        Nloc=re.search("Number of monomers: ",text).end()
        #print(text[Nloc:Nloc+2])
        
        try:
            N_File=int(text[Nloc:Nloc+3])
        except:
            N_File=int(text[Nloc:Nloc+2])
        try:

        # append the values to the arrays:
            N=np.append(N,N_File)
        #print(N_File)
            print(2*np.loadtxt(File,skiprows=19,unpack=True)[4][100:])
            Rg2 = np.loadtxt(File,skiprows=19,unpack=True)[4][110:]
            Rg2mean = np.append(Rg2mean,Rg2.mean())
            ErrRg2 = np.append(ErrRg2,Rg2.std())
        except:
            print(File)
            break

def potfit(xdata, ydata,yerr, ampstart=1, expstart=1):
    """
    Fits and plots a powerlaw to ydata(xdata), w.r.t.
    x=amp*x**(index). 

    """
    logx = np.log10(xdata)
    logy = np.log10(ydata)
    logyerr = np.log10(yerr)#/ydata
   
    
    # Define function for calculating a power law
    powerlaw = lambda x, amp, index: amp * (x**index)
    # define our (line) fitting function
    fitfunc = lambda p, x: p[0] + p[1] * x
    errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err

    pinit = [1.0, 1.2]
    out = optimize.leastsq(errfunc, pinit,
                       args=(logx, logy, logyerr), full_output=1)

    pfinal = out[0]
    covar = out[1]
    print( pfinal)
    print( covar)

    index = pfinal[1]
    amp = 10.0**pfinal[0]

    indexErr = np.sqrt( covar[1][1] )
    ampErr = np.sqrt( covar[0][0] ) * amp
    
    plt.clf()
    plt.subplot(2, 1, 1)
    plt.plot(xdata, powerlaw(xdata, amp, index), label=r"Fitting Function: $R(N)=R_0\cdot N^\sigma$ ")     # Fit
    plt.errorbar(xdata, ydata, yerr=yerr, fmt='k.')  # Data
    plt.text(50,2000,r'$R_0$ = %5.2f$\pm$0.1' % (amp), fontsize=10) 
    plt.text(50,1000 ,r'$\sigma$ = %5.2f$\pm$0.01' % (index), fontsize=10)
    plt.legend(loc='lower right')
    plt.title('R(N) scaling fit')
    plt.xlabel('N')
    plt.ylabel(r'$R^2$')
    #plt.xlim(1, 11)

    plt.subplot(2, 1, 2)
    plt.loglog(xdata, powerlaw(xdata, amp, index))
    plt.errorbar(xdata, ydata, yerr=yerr, fmt='k.')  # Data
    plt.xlabel('N (log scale)')
    plt.ylabel(r'$R^2$ (log scale)')
    #plt.xlim(, 11)
    print('Die Amplitude ist {} +- {} und der Exponent beträgt {} +- {}. '.format(amp, ampErr, index, indexErr))
    plt.show()


#for i in [N,Rg2mean,ErrRg2]:
#    print(np.size(i))
#  sort the data:
sort = np.argsort(N)
N, Rg2mean, ErrRg2 = N[sort], Rg2mean[sort], ErrRg2[sort]

# save array to text:

data = np.transpose(np.array([N,Rg2mean,ErrRg2]))
np.savetxt("R-N-Scaling.dat", data, delimiter= "     ", fmt="%-1.3f",
            header="N            Rg2mean      delta(Rg2mean) (stdev) ")




#output = np.concatenate((N,Rg2mean), axis=0)
#output = ErrRg2
#np.savetxt("R-N-scaling.dat",output)

# fit and plot:
potfit(N,Rg2mean,ErrRg2)





#sort = np.argsort(N)
#N, Rg2mean, ErrRg2 = N[sort], Rg2mean[sort], ErrRg2[sort]
#plt.figure()
#plt.errorbar(N,Rg2mean,yerr=ErrRg2)
#plt.show()
#print(Rg2mean,N,ErrRg2)



