#Fixed XOR

### FUNCTIONS ###

def xor_hex_string(HEX1, HEX2):
    #returns xor of two hex bytes as a hex byte
    HEX = []
    for h1, h2 in zip(HEX1, HEX2):
        HEX.append(ord(hex(int(chr(h1),16)^int(chr(h2),16))[2:]))
    return bytes(HEX)

### MAIN PROGRAM ###

def main():
    #inputs
    HEX1 = b'1c0111001f010100061a024b53535009181c'
    HEX2 = b'686974207468652062756c6c277320657965'

    #output
    HEX = xor_hex_string(HEX1, HEX2)

    assert(HEX == b'746865206b696420646f6e277420706c6179')

if __name__ == '__main__':
    main()
