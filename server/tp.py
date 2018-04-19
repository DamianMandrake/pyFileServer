import sys;
sys.path.append("..");

import utils
currentfile = open('/home/rohan/Documents/c_workspace/temp/tp.c', 'rb')

data = bytearray()
try:

    bytes = []
    byte = currentfile.read(1)
    print("DONE");
    temp = bytearray()

    while byte :
        print(byte)
        bytes.append(byte)
        byte = currentfile.read(1)

except Exception as e:
    raise e
finally:
    currentfile.close()

print(bytes)
temp = bytearray();
for i in range (0,len(bytes)):
    temp.append(bytes[i])
    if i % 4 == 0:
        data.append(utils.utilities.ByteHandler.bytesToInt(temp))
        temp = bytearray()



print(data)

