#AES in ECB mode

from Crypto.Cipher import AES
import base64

### MAIN PROGRAM ###

def main():
    encoded = []
    print('Loading file contents...')
    with open('c7_file.txt', 'rt') as f:
        for l in f:
            encoded.append(l[:-1])
    encoded = bytes(''.join(encoded), 'utf_8')
    encoded = base64.b64decode(encoded)
    print('Done')

    key = b'YELLOW SUBMARINE'

    cipher = AES.new(key, AES.MODE_ECB)

    decrypt = cipher.decrypt(encoded)

    print(decrypt.decode())


if __name__ == '__main__':
    main()
