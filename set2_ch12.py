from os import urandom              # to generate 'bytes'
from Crypto.Cipher import AES
from set2_ch9 import pad
from base64 import b64decode
from set2_ch10 import ECBEncrypt, ECBDecrypt
from set1_ch8 import hasRepBlocks

BLOCK_SIZE = AES.block_size
KEY = urandom(BLOCK_SIZE)

def encryption_oracle(input: bytes):
    # unknown string that will be added to input string
    unknownString = b'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'
    # append decoded unknown string to input
    plaintext = input + b64decode(unknownString)
    # encrypt plaintext with ECB mode
    ciphertext = ECBEncrypt(pad(plaintext, BLOCK_SIZE), KEY)         # pad plaintext for successful encryption

    return ciphertext

def getBlockSize(OracleEncryption):
    # size of cihpertext encrypted via encryption_oracle with 0-bytes input
    size = len(OracleEncryption(b''))
    # to store new size of ciphertext
    newSize = 0
    # number of indentical bytes fed
    byte = 1
    while True:
        # indentical bytes to be fed
        identicalBytes = b'A' * byte
        # get new size of of ciphertext via encryption_oracle with identicalBytes as input
        newSize = len(OracleEncryption(identicalBytes))   
        if size != newSize:             # break if both sizes are different
            break
        byte += 1                       # increment bytes by 1
    # get block size by substracting size from new size of ciphertext
    blockSize = newSize - size  

    return blockSize

def decryptUnknownString(OracleEncryption, unknownStringSize):
    # to detect if encryption is ECB
    myStr = b'mystring' * (BLOCK_SIZE * 2 + 100)    # 100 is jsut a random number

    # Encryption is ECB if has duplicate blocks
    if hasRepBlocks(OracleEncryption(myStr)):
        # indentical bytes to be fed with same size of unknown string
        identicalBytes = b'A' * unknownStringSize
        # to store unknown string
        unknownString = b''
        for i in range(unknownStringSize):
            # shorten indentical bytes by 1 character ('A')
            idenBytes = identicalBytes[:-i]
            # encrypt oracle using encryption_oracle with identical bytes input
            ciphertext = OracleEncryption(idenBytes)
            # to be compared with ciphertext of block encrypted
            toBeCompared = ciphertext[:unknownStringSize]
            
            for byte in range(256):                # there are 256 bytes values
                # put together identical bytes with unknown string and current byte
                block = idenBytes + unknownString + bytes([byte])
                # compare ciphertext of block encrypted with toBeCompared
                # and break if they are identical
                if OracleEncryption(block)[:unknownStringSize] == toBeCompared:
                    unknownString += bytes([byte])
                    break
        return unknownString 
    else:
        return "Not ECB"



def main():
    # block size of Oracle Encryption
    blockSize = getBlockSize(encryption_oracle)
    print("BLOCK SIZE:", blockSize)  

    # size of unknown string
    unkStrSize = len(encryption_oracle(b''))
    # get unknown string
    unknownString = decryptUnknownString(encryption_oracle, unkStrSize)
    print("\nUNKNOWN STRING:")
    print(unknownString.decode())


    return 0

if __name__ == '__main__':
    main()