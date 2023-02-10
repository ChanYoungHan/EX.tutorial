import os
import struct

path = "float.bin"
f = open(path, "rb")
num = f.read()
print(num, len(num))

b1 = num[:4]
for n in range(0, len(num) // 4):
    b1 = num[n * 4 : (n + 1) * 4]
    print(b1, type(b1), len(b1))
    print(struct.unpack("f", b1))


path = "int.bin"
f = open(path, "rb")
num = f.read()
print(num, len(num))

b1 = num[:1]
for n in range(0, len(num) // 1):
    b1 = num[n * 1 : (n + 1) * 1]
    print(b1, type(b1), len(b1))
    print(struct.unpack("B", b1))
