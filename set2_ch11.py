from random import randint
from os import urandom              # to generate 'bytes'
from Crypto.Cipher import AES

from set2_ch9 import pad
from set2_ch10 import ECBEncrypt
from set2_ch10 import CBCEncrypt
from set1_ch8 import hasRepBlocks

BLOCK_SIZE = AES.block_size    # AES uses 16-bytes block size

def encryption_oracle(input: bytes):
    # generate random key of class 'bytes'
    key = urandom(16)
    # add random bytes in front and at the end of input
    plaintext = urandom(randint(5,10)) + input + urandom(randint(5,10))

    # chose type of encryption randomly
    if randint(0,1):
        ciphertext = ECBEncrypt(pad(plaintext, BLOCK_SIZE), key)         # pad plaintext for successful encryption
        print("Encryption used ECB")
        return ciphertext
    else:
        # generate random iv of class 'bytes'
        iv = urandom(16)
        ciphertext = CBCEncrypt(pad(plaintext, BLOCK_SIZE), key, iv)     # pad plaintext for successful encryption
        print("Encryption used CBC")
        return ciphertext

def detectEncryption(ciphertext: bytes):     
    # ECB encryption if ciphertext has duplicate blocks
    if hasRepBlocks(ciphertext):
        return "*Detected ECB encryption*"
    # CBC encryption if not
    else:
        return "*Detected CBC encryption*"

def main():

    # Plaintext needs to have duplicate blocks to find ECB encryption
    # and it has to be more than 32 bytes (BLOCK_SIZE * 2) length since
    # random bytes are appended in front and at the end of it 
    plaintext = ("CPSC487"*(BLOCK_SIZE * 2 + randint(1, 100))).encode()                   # added between 1 and 100 for testing - encode() to use 'bytes'
    
    # ciphertext after being encrypted with ECB or CBC
    ciphertext = encryption_oracle(plaintext)
    
    # Detect type of ecnryption
    print(detectEncryption(ciphertext))

    return 0

if __name__ == '__main__':
    main()