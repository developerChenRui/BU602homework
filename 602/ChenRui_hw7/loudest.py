# Copyright 2017 ChenRui ruirui@bu.edu
# Copyright 2017 mengxi wang wmx@bu.edu
# Copyright 2017 Chunxi Wang tracycxw@bu.edu
import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as pyplot

def loudest_band(music,frame_rate,bandwidth):
    N=len(music)
    f= np.arange(-frame_rate/2, frame_rate/2, float(frame_rate)/N)#0.1 is frame_rate/N
    
    zero_index = np.absolute(f).argmin()
    
    fourier_f_music=np.fft.fft(music)
    fourier_f=np.fft.fftshift(fourier_f_music)
    f_y=np.power(np.absolute(fourier_f),2)
    
    #design window
    window_width=int(bandwidth/(float(frame_rate)/N))
#    sum_f=np.sum(f_y[zero_index:zero_index+window_width]) 
    
    max_f=0
    max_f_index=0
    for i in range(zero_index,N-window_width):
        sum_f=np.sum(f_y[i:i+window_width]) 
        
        if max_f<sum_f:
            max_f=sum_f
            max_f_index=i
    
    low=(max_f_index-zero_index)*frame_rate/N
    high=(max_f_index-zero_index+window_width)*frame_rate/N
            
    H = np.zeros(N)
    for i in range(max_f_index,max_f_index+window_width):
        H[i] = 1
        
    left_low = zero_index-(max_f_index-zero_index)-window_width

    
    for i in range(left_low,left_low+window_width):
        H[i] = 1
#    pyplot.plot(fourier_f)
#    pyplot.plot(H)
    fft_filtered = np.multiply(fourier_f,H)
#    pyplot.plot(fft_filtered)
    loudest = np.fft.ifft(np.fft.ifftshift(fft_filtered))
#    pyplot.plot(loudest)    
#	loudest = np.fft.ifft(np.fft.ifftshift(fft_filtered))
    return (low, high, np.real(loudest))
    
    
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
#    pyplot.plot(music[:,0])
#    pyplot.plot(loudest)
    pyplot.plot(np.fft.fft(loudest))
if __name__ == '__main__':
    main()
