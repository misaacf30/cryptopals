import requests
from base64 import b64decode
from Crypto.Cipher import AES
from set2_ch15 import unpad

BLOCK_SIZE = AES.block_size    # AES uses 16-bytes block size     

def xor(var, key):
    return bytes(a ^ b for a, b in zip(var, key))

def ECBEncrypt(plaintext: bytes, key: bytes):
    cipher = AES.new(key, AES.MODE_ECB)             # cipher that is used to ecnrypt plaintext (AES  in ECB mode)
    ciphertext = cipher.encrypt(plaintext)          # encrypt plaintext using cipher
    return ciphertext

def ECBDecrypt(ciphertext: bytes, key: bytes):
    cipher = AES.new(key,  AES.MODE_ECB)            # cipher that is used to decrypt ciphertext (AES  in ECB mode)
    plaintext = cipher.decrypt(ciphertext)          # decrypt ciphertext using cipher
    return plaintext

def CBCEncrypt(message: bytes, key: bytes, iv: bytes):
    ciphertext = b''                        # to store ciphertext in 'bytes'
    prevCtBlock = iv                        # contains previous ciphertext block (first one is iv)

    for i in range(0, len(message), BLOCK_SIZE):                # from 0 to message length incrementing block size (16)
        xored = xor(message[i: i+BLOCK_SIZE], prevCtBlock)      # xor current block with previous block
        ciphertext += ECBEncrypt(xored, key)                    # concatenate ECB encryption result into ciphertext
        prevCtBlock = ciphertext[i: i+BLOCK_SIZE]               # previous block becomes current block for next iteration

    return ciphertext

def CBCDecrypt(ciphertext: bytes, key: bytes, iv: bytes):
    plaintext = b''                         # to store plaintext in 'bytes'
    prevCtBlock = iv                        # contains previous ciphertext block (first one is iv)

    for i in range(0, len(ciphertext), BLOCK_SIZE):             # from 0 to ciphertext length incrementing block size (16)
        xored = xor(ECBDecrypt(bytes(ciphertext[i: i + AES.block_size]), key), prevCtBlock)     # xor ECB encryption result with previus block
        plaintext += xored                                      # concatenate result of XOR operation with plaintext
        prevCtBlock = ciphertext[i: i + BLOCK_SIZE]             # previous block becomes current block for next iteration

    return unpad(plaintext, BLOCK_SIZE)             # unpad() to remove padding of plaintext

def main():
    # make a request to the challenges web page to get file and store text
    URL = 'https://cryptopals.com/static/challenge-data/10.txt'
    text = requests.get(URL).text               # base64 ('str')
    ciphertext = b64decode(text)                # bytes
    
    # key used to decrypt ciphertext in 'bytes'
    key = b'YELLOW SUBMARINE'
    # iv used to decrypt ciphertext in 'bytes'
    iv = b'\x00' * BLOCK_SIZE 

    plaintext = CBCDecrypt(ciphertext, key, iv)
    print(plaintext.decode())                       # decode() to get string format

    return 0

if __name__ == '__main__':
    main()