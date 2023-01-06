import wave, struct
import matplotlib.pyplot as plt
import numpy as np
import os

# this program can plot any wav file

dir = '../samples'

for filename in os.listdir(dir):
    file = os.path.join(dir, filename)
    wavefile = wave.open(file, 'rb')
    wavedata = wavefile.readframes(wavefile.getnframes())
    data = struct.unpack("<" + str(wavefile.getnframes()) + "h", wavedata)
    data_array = np.asarray(data)

    plt.plot(data_array, '-', linewidth = 0.25)
    plt.legend()
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.savefig('plots/' + filename[0:2] + '.png', dpi=200)
    plt.clf()
