import requests
from base64 import b64decode
from set1_ch3 import getKey             # to get key character
from set1_ch5 import repeatingKeyXOR
import codecs

def stringToBinary(str):
    return ''.join(format(ord(i), '08b') for i in str)          # convert string to binary format without spaces

def xorBinary(a, b):                    # parameters: 'binary'
    result = ""                                     # to store binary result after xor'd
    if len(a) == len(b):
        for i in range(len(a)):
            xor = int(a[i]) ^ int(b[i])             # xor each element of a with each element of b at index i
            result = result + str(xor)              # concatenate result string with each xor'd value
        return result
    return 0

def hammingDistance(a, b):
    xor = xorBinary(stringToBinary(a), stringToBinary(b))       # xor a with b in binary format
    count = 0
    for i in range(len(xor)):                       # count num of 1's
        if xor[i] == "1":                           # if character of xor'd value is 1
            count = count + 1                       # add 1 to count
    return count

def scoreKey(keySize, ciphertext):
    blockSize = 2 * keySize                             # size of each block
    blocks = len(ciphertext) // blockSize - 1           # number of blocks
    score = 0                                           # score of key size

    for i in range(blocks):
        # Blocks' slices
        blockA = slice(i * blockSize, i * blockSize + keySize)
        blockB = slice(i * blockSize + keySize, i * blockSize + 2 * keySize)
        # Hamming distance between blocks
        hamDis = hammingDistance(stringToBinary(ciphertext[blockA].decode("utf-8")), stringToBinary(ciphertext[blockB].decode("utf-8")))
        score += hamDis

    # Normalize score result
    score = (score / keySize) / blocks
    return score

def findKeySize(ciphertext, start, end):
    lowest =  scoreKey(start, ciphertext)           # to store lowest score
    keySize = 0                                     # to store key length with lowest score

    for i in range(start, end+1):
        score = scoreKey(i, ciphertext)             # to store scores
        if score < lowest:                          # if computed score is lower that lowest score
            lowest = score                          # store new lowest score
            keySize = i                             # store new key size
    return keySize


def findKey(ciphertext, keySize):
    transposed = tuple([] for _ in range(keySize))  # transposed tuple with same size as the key
    t = 0                                           # index of transposed item
    for i in range(len(ciphertext)):                # iterates through the whole ciphertext
       transposed[t].append(ciphertext[i])          # append first byte of every transposed item, second byte of every transposed item, and so on.  
       t = t + 1                                    # increment t
       if t == keySize:                             # start over if t is same as key size
        t = 0
    key = ""                                        # to store key characters and put them together
    for i in range(len(transposed)):                # go through each transposed item
        keyChr = chr(getKey(transposed[i]))         # parameter: smallCiphertext=transposed[i] -> 'bytes'
        key = key + keyChr                          # concatenate the key with each key character gotten
    return key


def main():
    # make a request to the challenges web page to get file and store text
    URL = 'https://cryptopals.com/static/challenge-data/6.txt'
    text = requests.get(URL).text               # base64
    ciphertext = b64decode(text)                # bytes 

    # find the size of key used to de decrypt ciphertext
    keySize = findKeySize(ciphertext, 2, 41)

    # find key used to decrypt ciphertext
    key = findKey(ciphertext, keySize)
    
    # get plaintext by using breaking repeating key XOR
    plaintext_hex = repeatingKeyXOR(ciphertext.decode('utf-8'), key)       # plaintext in hex format
    plaintext_binary = codecs.decode(plaintext_hex, "hex")                 # plaintext in 'bytes' format
    plaintext_str = str(plaintext_binary,'utf-8')                          # plaintext in 'str' format

    # OUTPUT
    print("KEY ->", key)
    print("\nPLAINTEXT:\n")
    print(plaintext_str)

    return 0

if __name__ == '__main__':
    main()