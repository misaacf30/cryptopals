import requests
from binascii import unhexlify

BLOCK_SIZE = 16                 # size of each block

def hasRepBlocks(ciphertext):
    blocks = []                                                     # to store blocks of each ciphertext
    blockNum = int(len(ciphertext)/BLOCK_SIZE)                      # number of blocks
    
    for i in range(blockNum):
        blocks.append(ciphertext[i*BLOCK_SIZE:(i+1)*BLOCK_SIZE])    # append blocks of 16 bytes to blocks list

    # convert blocks list to set, and duplicates are NOT allowed
    if(blockNum != len(set(blocks))):                               # if set size is different from number of blocks
        return True                                                 # means that there are repeated blocks
    else:                                                           # which demonstrates high possiblities
        return False                                                # of being encrypted with AES ECB mode

def main():
    # make a request to the challenges web page to get file and store text
    URL = 'https://cryptopals.com/static/challenge-data/8.txt'
    txt = requests.get(URL).text                        # 'str'
    ciphertexts = txt.split()                           # 'list' of hex values, by default split() separator is white space
    ciphertexts = [unhexlify(c) for c in ciphertexts]   # 'list' of bytes

    ciphertextsFound = []                               # to store ciphertexts encrpted with ECB
    
    # iterates through all ciphertexts to find ciphertext with repeated blocks
    for i in range(len(ciphertexts)):
        if hasRepBlocks(ciphertexts[i]) == True:
            ciphertextsFound.append(ciphertexts[i])     # append ciphertext with repetead blocks

    print("Ciphertext encrypted with ECB:")
    print(ciphertextsFound)

    return 0

if __name__ == '__main__':
    main()

