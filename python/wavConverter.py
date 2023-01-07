import wave, struct
import numpy as np
import os

# this program saves all 16 bit wav samples to binary format

dir = '../samples'

for filename in os.listdir(dir):
    file = os.path.join(dir, filename)
    wavefile = wave.open(file, 'rb')
    wavedata = wavefile.readframes(wavefile.getnframes())
    data = struct.unpack("<" + str(wavefile.getnframes()) + "h", wavedata)
    data_array = np.asarray(data)
    data_array.astype('int16').tofile('../src/samples_bin/' + filename[0:2] + '.bin')
