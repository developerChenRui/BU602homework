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

def get_f0(data, fs):
    w = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(w))
#    freqs = np.square(freqs)
#    high = freqs.max()
#    low = freqs.min()
    idx = np.argmax(np.abs(w))
    freq = freqs[idx]
    freq_in_hertz = abs(freq * fs)
#    check1 = np.argmax(w)
#    check2 = len(data)
#    check3 = fs
#    return np.argmax(w)*len(data)/fs
    return freq_in_hertz
    
def loudest_band(music,frame_rate,bandwidth):
    f_0 = get_f0(music, frame_rate)
    low = f_0 - bandwidth/2
    high = f_0 + bandwidth/2
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
    fname = "bach10sec.wav"
    music,frame_rate,nframes,nchannels = read_wave(fname,debug=True)
    bandwidth = 500
    low,high,loudest = loudest_band(music[:,0],frame_rate,bandwidth)
    pyplot.plot(np.fft.fft(music[:,0]))
    pyplot.plot(loudest)
    pyplot.plot(np.fft.fft(loudest))
    
    wav.write("loudest.wav", frame_rate, loudest)
    
    
    print(low,high,loudest)
    
if __name__ == '__main__':
    main()