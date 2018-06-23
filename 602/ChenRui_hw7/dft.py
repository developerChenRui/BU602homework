# Copyright 2017 mengxi wang wmx@bu.edu
# Copyright 2017 ChenRui ruirui@bu.edu
from numpy import zeros, exp, array, pi

    
def DFT(x):
    try:
#        xarray = [float(i) for i in x]
        X = []
        for k in range(len(x)):
        	sum_N = 0
        	for n in range(len(x)): 
        		sum_N = sum_N + x[n]*exp(-1j*2*pi*n*k/len(x)) 
        	X.append(sum_N)
        return array(X)
    except:
        raise ValueError
    

        
    

def main():
    print(DFT([0,1,2]))
#    print(fft([0,1,2]))
#    print(np.fft.fft([0,1,2]))


if __name__ == '__main__':
  main()
    
