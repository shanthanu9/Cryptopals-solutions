#Fixed XOR

### FUNCTIONS ###

def xor_hex_string(HEX1, HEX2):
    #returns xor of two hex equivalent strings as 
    # hex equivalent string
    return bytes([hex1 ^ hex2 for hex1, hex2 in zip(HEX1, HEX2)])

### MAIN PROGRAM ###

def main():
    #inputs
    HEX1 = bytes.fromhex('1c0111001f010100061a024b53535009181c')  #returns hex equivalent
    HEX2 = bytes.fromhex('686974207468652062756c6c277320657965')

    #output
    HEX = xor_hex_string(HEX1, HEX2)    

    assert(HEX.hex() == '746865206b696420646f6e277420706c6179')

if __name__ == '__main__':
    main()
