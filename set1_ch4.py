#import string
import requests
from set1_ch3 import singleByteXOR, getScore, getKey

def main():
    # make a request to the challenges web page to get file and store strings into list
    URL = 'https://cryptopals.com/static/challenge-data/4.txt'
    text = requests.get(URL).text.split("\n")
    text = list(map(bytes.fromhex, text))

    highestScore = 0
    result = ''
    for i in text:
        ciphertext = i                                      # bytes format
        key = getKey(ciphertext)                            # key used to decrypt message
        score = getScore(singleByteXOR(ciphertext, key))    # score after xor ciphertext with single character (key)

        # store result if has higher score than others decrypted messages
        if score > highestScore:
            highestScore = score
            result = singleByteXOR(ciphertext, key)

    # print decrpyted message that has best score for letter frequency
    print(result.decode())

    return 0

if __name__ == '__main__':
    main()