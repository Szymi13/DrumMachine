import matplotlib.pyplot as plt
import os
import struct

with open("../src/for_testing.txt", mode="rb") as file:
    fileContent = file.read()

a = struct.unpack("h" * ((len(fileContent)) // 2), fileContent)
plt.plot(a)
plt.show()
