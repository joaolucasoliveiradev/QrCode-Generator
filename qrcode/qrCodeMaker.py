class qrCodeMaker:
    def __init__(self):
        self.__bit = ""

    def initEncodeCode(self):
        self.bit = "0100"
        return self.bit

    def stringToBit(self, msg:str):
        to_bits = ""
        temp = ""
        convert_char = 0
        len_bit_message = str(f"{len(msg):b}")
        while len(len_bit_message) < 8:
            len_bit_message = "0" + len_bit_message
        for char in msg:
            convert_char = ord(char)
            temp = str(f"{convert_char:b}")
            while len(temp) < 8:
                temp = "0" + temp
            to_bits+=temp
        self.bit += len_bit_message
        self.bit += to_bits
        return self.bit

    def getBits(self):
        return self.bit