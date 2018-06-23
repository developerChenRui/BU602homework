#Copyright 2017 mengxi wang wmx@bu.edu
import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

def loudest_band(music,frame_rate,bandwidth):
    N=len(music)
    f= np.arange(-frame_rate/2, frame_rate/2, 0.1)#0.1 is frame_rate/N
    zero_index = np.absolute(f).argmin()
    
    fourier_f=np.fft.fft(music)
    fourier_f=np.fft.fftshift(fourier_f)
    f_y=np.power(np.absolute(fourier_f))

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
    loudest=butter_bandpass_filter(music, low, high, frame_rate, order=5)
#    loudest = np.real(np.fft.ifft(np.fft.ifftshift(fft_filtered)))
    return (low, high, loudest)
    
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)   
    return y
    
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
    
if __name__ == '__main__':
    main()