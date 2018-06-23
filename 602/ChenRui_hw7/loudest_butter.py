#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:55:15 2017

@author: chenrui
"""
import scipy.io.wavfile as wavfile
import scipy.io.wavfile as wav
import numpy as np
from scipy.signal import butter, lfilter
from numpy import zeros, exp, array, pi
import matplotlib.pyplot as pyplot

def get_f_low(data, fs,bandwidth):
    N=len(data)
    f= np.arange(-fs/2, fs/2, 0.1)#0.1 is frame_rate/N
    
    zero_index = np.absolute(f).argmin()
    
    fourier_f_music=np.fft.fft(data)
    fourier_f=np.fft.fftshift(fourier_f_music)
    f_y=np.power(np.absolute(fourier_f),2)
    
    #design window
    window_width=int(bandwidth/0.1)
    sum_f=np.sum(f_y[zero_index:zero_index+window_width]) 
    
    max_f=0
    max_f_index=0
    for i in range(zero_index,N-window_width):
        sum_f=np.sum(f_y[i:i+window_width]) 
        if max_f<sum_f:
            max_f=sum_f
            max_f_index=i
    
    return (max_f_index-zero_index)*fs/N
    
def loudest_band(music,frame_rate,bandwidth):
    f_l = get_f_low(music, frame_rate,bandwidth)
    low = f_l
    high = f_l + bandwidth
    loudest = butter_bandpass_filter(music,low,high,frame_rate)
    return low,high,loudest

def read_wave(fname,debug=False):
    "return a time signal read from the WAV file fname"
    frame_rate,music = wavfile.read(fname)
    if debug:
        print(frame_rate,type(music),music.shape,music.ndim)
    if music.ndim>1:
        nframes,nchannels = music.shape
    else:
        nchannels = 1
        nframes = music.shape[0]    
    return music,frame_rate,nframes,nchannels

def butter_bandpass(lowcut, highcut, fs, order=1):
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
    fname = "bach10sec.wav"
    music,frame_rate,nframes,nchannels = read_wave(fname,debug=True)
    bandwidth = 500
    low,high,loudest = loudest_band(music[:,0],frame_rate,bandwidth)
    pyplot.plot(np.fft.fft(music[:,0]))
#    pyplot.plot(loudest)
    pyplot.plot(np.fft.fft(loudest))
    
    wav.write("loudest.wav", frame_rate, loudest)
    
    
    print(low,high,loudest)
    
if __name__ == '__main__':
    main()