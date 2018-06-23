# Copyright 2017 mengxi wang wmx@bu.edu
# Copyright 2017 ChenRui ruirui@bu.edu
import numpy as np
import scipy.io.wavfile as wav

def dialer(file_name,frame_rate,phone,tone_time):
    t = np.arange(0,tone_time,1.0/frame_rate) 
    tones={'1': [697,1209],
		'2': [697,1336],
		'3': [697,1477],
		'4': [770,1209],
		'5': [770,1336],
		'6': [770,1477],
		'7': [852,1209],
		'8': [852,1336],
		'9': [852,1477],
		'0': [941,1336],
         '*': [941,1209],
         '#': [941,1477]
        }
    dial_signal=[];
    for i in phone:
        f = tones[i]
        signal = (np.sin(2*np.pi*f[0]*t) + np.sin(2*np.pi*f[1]*t))/2
        dial_signal=np.append(dial_signal,signal)
    wav.write(file_name, frame_rate, dial_signal)

def main():
    file_name="bell.wav"
    frame_rate=41000
    phone="13985610731"
    tone_time=0.15
    dialer(file_name,frame_rate,phone,tone_time)
    
if __name__ == '__main__':
    main()
