def xor(a, b):
    if(len(a) == len(b)):                               # if values length are equal
        # xor first value with second value
        result = hex(int(a, 16) ^ int(b, 16)) [2:]      # don't return first 2 values (0x)
        if len(result) == 1:                            # **needed for challenge #5**
            result = "0" + result                       # add character '0' to result with only one character
        return result                       
    else:
        return 0                                        # return 0 if values length are different

def main():
    hex1 = "1c0111001f010100061a024b53535009181c"
    hex2 = "686974207468652062756c6c277320657965"
    print(xor(hex1,hex2))

    return 0

if __name__ == '__main__':
    main()