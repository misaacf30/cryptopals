def pad(message: bytes, block_size:int):
    # num of padding bytes added ('int')
    numPaddingBytes = block_size - (len(message) % block_size)
    # value of padding byte
    padding = bytes([numPaddingBytes])        # bytes([4]) -> b'\x04'     !=      bytes(4) ->  b'\x00\x00\x00\x00'
    # whole padding
    padding = padding * numPaddingBytes 
    # message with padding
    paddedMessage = message + padding

    return paddedMessage

def main():       
    message = b'YELLOW SUBMARINE'          # size = 16 bytes
    blockSize = 20                         # irregular size
  
    print(pad(message, blockSize))

    return 0

if __name__ == '__main__':
    main()