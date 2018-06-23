#Copyright 2017 mengxi wang wmx@bu.edu
import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as pyplot


def loudest_band(music,frame_rate,bandwidth):
    N=len(music)
    f= np.arange(-frame_rate/2, frame_rate/2, 0.1)#0.1 is frame_rate/N
    zero_index = np.absolute(f).argmin()
    
    fourier_f=np.fft.fft(music)
    fourier_f=np.fft.fftshift(fourier_f)
    f_y=np.square(np.absolute(fourier_f))
    
    #design window
    window_width=int(bandwidth/0.1)
    sum_f=np.sum(f_y[zero_index-1:zero_index+window_width])
    
    max_f=0
    max_f_index=0
    for i in range(zero_index,N-window_width):
        sum_f=sum_f-(f_y[i-1]-f_y[window_width+i-1])
        if max_f<sum_f:
            max_f=sum_f
            max_f_index=i
    
    low=(max_f_index-zero_index)*frame_rate/N
    high=(max_f_index-zero_index+window_width)*frame_rate/N
            
    H = np.zeros(N)
    for i in range(max_f_index,max_f_index+window_width+1):
        H[i] = 1
	fft_filtered = fourier_f*H
	loudest = np.real(np.fft.ifft(np.fft.ifftshift(fft_filtered)))
	
	return (low, high, loudest)
    
    
def main():
    file_name='bach10sec.wav'
    frame_rate,music=wav.read(file_name,False)
    bandwidth=500
    (low,high,loudest)=loudest_band(music[:,0],frame_rate,bandwidth)
    
    print(low)
    print(high)

    loudest = loudest.astype(np.float32) #convert to 32-bit float\
    wav.write(file_name[0:-4]+'_filtered.wav',frame_rate,loudest)
#    print(music[:,0].shape)
#    print(music.shape)
    pyplot.plot(np.fft.fft(music[:,0]))
#    pyplot.plot(loudest)
    pyplot.plot(np.fft.fft(loudest))
if __name__ == '__main__':
    main()