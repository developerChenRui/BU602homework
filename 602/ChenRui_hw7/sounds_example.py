# Support for sound is provided 
# in a number of modules. Some
# are part of the standard library,
# but others are not. Everything we 
# use is part of the Anaconda distribution
# of python.

# WAV file support
import scipy.io.wavfile as wavfile

# sound playing
import subprocess
def play(fname):
	subprocess.run(['aplay',fname])

# sleep while sound is playing
from time import sleep

# arrays
import numpy

# plotting facilities
import matplotlib.pyplot as pyplot

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



fname = "bach10sec.wav"

# Plot the sound
music,frame_rate,nframes,nchannels = read_wave(fname,debug=True)
if nchannels > 1:
    music = music.sum(axis=1)

pyplot.plot(music[:44100])
pyplot.title('First second of bach music')
print('Close plot in Figure 1 to continue...')
pyplot.show()

# Listen to the sound
#play('bach10sec.wav')
#play('scary.wav')
