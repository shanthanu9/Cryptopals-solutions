# Implement CBC mode

from Crypto.Cipher import AES
from c9 import PKCS_pad
import base64

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


def decrypt_CBC(cipher_text, IV, key):
    # to decrypt CBC
    # IV is the initialization vector
    # NOTE: the plaintext must be padded
    # to len(key)

    block_size = len(key)

    cipher = AES.new(key, AES.MODE_ECB)

    prev = IV
    plain_text = []

    for i in range(0, len(cipher_text), block_size):
        block = cipher_text[i:i+block_size]
        inter = cipher.decrypt(block) # inter for intermediate stage
        plain_text.append(xor_two_strings(inter, prev))
        prev = block

    return b''.join(plain_text)

### MAIN PROGRAM ###

def main():

    encoded = []
    print('Loading contents in file...')
    with open('c10_file.txt') as f:
        for line in f:
            encoded.append(line[:-1])
    encoded = base64.b64decode(bytes(''.join(encoded), 'utf_8'))

    print('Done')

    key = b'YELLOW SUBMARINE'
    cipher_text = PKCS_pad(encoded, len(key))
    IV = b'\x00'*len(key)

    print('The plain text is : ')
    plain_text = decrypt_CBC(cipher_text, IV, key)

    print(plain_text.decode())


if __name__ == '__main__':
    main()
