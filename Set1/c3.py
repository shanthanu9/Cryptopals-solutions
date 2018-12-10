#Single-byte XOR cipher

import sys
sys.path.insert(0, '../')

import src
import math

### FUNCTIONS ### 

def xor_string_with_char(s, c):
    # each character of s is xor'ed with c(in ascii)

    return bytes([i^c for i in s])


def find_key(s):
    # find the character xor'ed to produce s
    
    l = []
    for i in range(0,256):
      	l.append(src.score_plaintext(xor_string_with_char(s, i)))

    key = l.index(min(l))
    return key

### MAIN PROGRAM ###

def main():
    #encoded string
    encoded = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    key = find_key(encoded)
    print("Key is", hex(key))
    print("Decoded string is:", xor_string_with_char(encoded, key).decode())

if __name__ == '__main__':
    main()
