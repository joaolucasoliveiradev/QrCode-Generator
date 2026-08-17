from qrCodeMaker import qrCodeMaker

def main():
    txt = "Hello World!"
    bit_message = qrCodeMaker()
    bit_message.initEncodeCode()
    bits = bit_message.stringToBit(txt)
    print(bits)

if __name__ == "__main__":
    main()