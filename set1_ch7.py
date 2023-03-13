import requests
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def main():
    # make a request to the challenges web page to get file and store text
    URL = 'https://cryptopals.com/static/challenge-data/7.txt'
    text = requests.get(URL).text               # base64
    ciphertext = b64decode(text)                # 'bytes'

    # key used to decrypt ciphertext in 'bytes'
    key = b'YELLOW SUBMARINE'

    # cipher that is used to decrypt ciphertext (AES  in ECB)
    cipher = AES.new(key, AES.MODE_ECB)

    # get plaintext by decrypting ciphertext using AES in ECB
    plaintext = cipher.decrypt(ciphertext)

    # use unpad() to remove standard padding from plaintext
    plaintext = unpad(plaintext, AES.block_size)

    print(plaintext.decode())

    return 0

if __name__ == '__main__':
    main()