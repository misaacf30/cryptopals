import base64

def hexToBase64(hex):
    # Decodes hex value into raw data
    raw = bytes.fromhex(hex)
    # Encodes it to base 64
    bs64 = base64.b64encode(raw)
    
    return bs64.decode('utf-8')         # Result in UTF-8 format is decoded 

def main():
    hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    print(hexToBase64(hex))
    return 0

if __name__ == '__main__':
    main()