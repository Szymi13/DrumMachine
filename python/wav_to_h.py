import wave
import numpy as np
import os
# this program saves all 16 bit wav samples to binary format

dir = '../samples'

for filename in os.listdir(dir):
    file = wave.open("../samples/" + filename)
    samples = file.getnframes()
    audio = file.readframes(samples)
    audio_as_arr= np.frombuffer(audio, dtype=np.int16)
