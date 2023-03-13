from Crypto.Cipher import AES

def unpad(paddedMessage: bytes, block_size: int):
    if not isValid(paddedMessage):
        return "Invalid"
    if not len(paddedMessage) % block_size:
        # last byte of message -> num of padding bytes added
        numPaddingBytes = paddedMessage[-1]
        # message without padding
        unpaddedMessage = paddedMessage[:-numPaddingBytes]
        return unpaddedMessage   
    else:
        return "Unpadded"

def isValid(paddegMessage: bytes):
    # last byte of message ('int')-> num of padding bytes added
    numPaddingBytes = paddegMessage[-1] 
    # padding of message provided
    currentPadding = paddegMessage[-numPaddingBytes:]
    # padding that message should have
    actualPadding = bytes([numPaddingBytes]) * numPaddingBytes

    return currentPadding == actualPadding


def main():
    # Plaintexts that will be unpadded
    plaintext1 = b'ICE ICE BABY\x04\x04\x04\x04'
    plaintext2 = b'ICE ICE BABY\x05\x05\x05\x05'
    plaintext3 = b'ICE ICE BABY\x01\x02\x03\x04'

    # Unpad plaintexts 
    print("Test1:", unpad(plaintext1, AES.block_size))
    print("Test2:", unpad(plaintext2, AES.block_size))
    print("Test3:", unpad(plaintext3, AES.block_size))

    return 0

if __name__ == '__main__':
    main()