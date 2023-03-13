import string

def singleByteXOR(ciphertext, key):                     # parameters: ciphertext->'bytes', key->'int'
    # xor ciphertext with single character (key)
    result = [x ^ key for x in ciphertext]
    return bytes(result)
    

def getScore(text):                                   # parameter: text->'bytes'
    score = 0
    text = text.lower()                               # lowercase
    frequentLetters = b"etaoin shrdlu"[::-1]          # reverse etaoin shrdlu
    
    for letter in text:
        if chr(letter) not in string.printable:      # if letter doesn't belong to printable characters
            return 0

        i = frequentLetters.find(letter)
        if i != -1:                                   # if value is found
            score += i  
    return score

def getKey(ciphertext):                 # parameter: ciphertex->'bytes'
    # return the value that has the highest score - more frequent letters
    return max(range(255), key = lambda x: getScore(singleByteXOR(ciphertext, x)))        # lambda = anonymous function

def main():
    ciphertext = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    key = getKey(ciphertext)                                # get key that decrypts message with more common letters
    print (singleByteXOR(ciphertext, key).decode())         # decode to delete bytes format

    return 0

if __name__ == '__main__':
    main()