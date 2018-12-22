# Implement CBC mode

from Crypto.Cipher import AES
from c9 import PKCS_pad

### FUNCTIONS ###

def xor_two_strings(a, b):
    # a and b are two byte strings
    # of same length
    # returns xor of both strings

    if len(a) != len(b):
        raise ValueError('Arguements to xor_two_strings must have same length')

    xor = []
    for i,j in zip(a, b):
        xor.append(i^j)

    return bytes(xor)


def encrypt_CBC(plain_text, IV, key):
    # to decrypt CBC
    # IV is the initialization vector

    block_length = len(key)
    s = PKCS_pad(plain_text, block_length)

    cipher = AES.new(key, AES.MODE_ECB)

    prev = IV

    encrpyt = []

    for i in range(0, len(s), block_size):
        block = xor_two_strings(s[i:i+block_size], prev)
        e = cipher.encrypt(block)
        encrypt.append(e)
        prev = e


### MAIN PROGRAM ###

def main():

    """encoded = []
    print('Load contents in file...')
    with open('c10_file.txt') as f:
        for line in f:
            encoded.append(line[:-1])
    encoded = bytes(''.join(encoded), 'utf_8')
    """

    plain_text = b'12345678901234567890'
    key = b'23456'
    IV = b'\x00\x00\x00\x00\x00'

    cipher = AES.new(key, AES.MODE_CBC)

    print(cipher.encrypt(plain_text))


if __name__ == '__main__':
    main()
