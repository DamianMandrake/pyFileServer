class ByteHandler:
    @staticmethod
    def bytesToInt(bytearray):
        print(len(bytearray))
        integer = 0
        integer = integer | (bytearray[3] << 24);
        integer = integer | (bytearray[2] << 16);
        integer = integer | (bytearray[1] << 8);
        integer = integer | bytearray[0]
        return integer;

    @staticmethod
    def intToBytes(integer):
        print(integer)
        firstByte = integer & 0xff
        secondByte = integer >> 8 & 0xff
        third = integer >> 16 & 0xff
        fourth = integer >> 24 & 0xff

        b = bytearray()
        b.append(firstByte)
        b.append(secondByte)
        b.append(third)
        b.append(fourth)
        return b
