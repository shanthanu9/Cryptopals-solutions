# An ECB/CBC detection oracle

from Crypto.Cipher import AES
from random import randint
from c9 import PKCS_pad

### GLOBAL VARIABLES ###

# AES-128 bit
BLOCK_SIZE = 16

### FUNCTIONS ###

def generateRandomBytes(n):
    # generates a random n byte string

    key = []
    for i in range(0,n):
        key.append(randint(0,255))

    return bytes(key)

def encryptionOracle(plaintext):
    # encrypt plaintext 50% of the time
    # in AES ECB mode and 50% of the time
    # in AES CBC mode
    
    # size of block
    block_size = BLOCK_SIZE

    # generate random key
    key = generateRandomBytes(block_size)

    begin = generateRandomBytes(randint(5,10))
    end = generateRandomBytes(randint(5,10))

    # add 5-10 bytes before and after plaintext
    s = begin + plaintext + end

    # pad
    s = PKCS_pad(s, block_size)

    # decide for ECB or CBC
    decide = randint(0,1)

    # ECB mode
    if decide == 0:
        cipher = AES.new(key, AES.MODE_ECB)
        return cipher.encrypt(s)

    # CBC mode
    else: 
        IV = generateRandomBytes(block_size)
        cipher = AES.new(key, AES.MODE_CBC, IV)
        return cipher.encrypt(s)

def oracle(ciphertext):
    # assumes ciphertext length is >= 48 bytes
    # simply compares 2nd and 3rd block

    block_size = BLOCK_SIZE

    if ciphertext[block_size:2*block_size] == ciphertext[2*block_size:3*block_size]:
        print('The ciphertext is EBC encrypted')
    else:
        print('The ciphertext is CBC encrypted')
    

### MAIN PROGRAM ###

def main():
    
    plaintext = b'A'*48
    print('Input plaintext :', plaintext)

    ciphertext = encryptionOracle(plaintext)

    print('Generated ciphertext :', ciphertext)

    oracle(ciphertext)

if __name__ == '__main__':
    main()
