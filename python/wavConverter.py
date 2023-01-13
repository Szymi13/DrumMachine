import wave, struct
import numpy as np
import os

dir = '../samples'

for filename in os.listdir(dir):
    file_to_write = open("../src/samples.h","a");
    file_to_write.write("extern const int16_t " + filename[0:2] + "[];\n\n",)


for filename in os.listdir(dir):
    file = os.path.join(dir, filename)
    wavefile = wave.open(file, 'rb')
    wavedata = wavefile.readframes(wavefile.getnframes())
    data = struct.unpack("<" + str(wavefile.getnframes()) + "h", wavedata)
    data_arr = []
    data_arr = np.asarray(data)

    fp = open("../src/samples.c","a")

    fp.write("const int16_t " + str(filename[0:2]) + ("[] = {"))

    with open("../src/samples.c", "a") as fp:
        for sample in data_arr:
          fp.write("%i, " % sample)


    fp = open("../src/samples.c","a")
    fp.write("};\n\n")
