from set1_ch2 import xor

def toHex(char):
    result = hex(ord(char))[2:]             # convert plaintext byte to hex
    if len(result) == 1:                    # if hex has only one character
        result = '0' + result               # add character '0' at the start of it
    return result

def repeatingKeyXOR(plaintext, key):                # parameters: plaintext->'str', key->'str
    k = 0                           # index of key
    ciphertext = ""                 # to store ecrypted stanza

    for i in plaintext:
        plainByte = i                                       # byte of plaintext     (1 char = 1 byte = 8 bits)
        keyByte = key[k]                                    # byte of key
        answer = xor(toHex(plainByte), toHex(keyByte))      # xor byte of plaintext with byte of key
        ciphertext = ciphertext + answer                    # concatenate encrypted bytes
        k += 1
        if k >= len(key):                   # if key index is out of bounds         (if k == 3: k = 0)
            k = 0                           # key index is at the start again
            
    return(ciphertext)

def main():
    plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    print(repeatingKeyXOR(plaintext, key))

    return 0

if __name__ == '__main__':
    main()