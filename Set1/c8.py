#Detect AES in ECB mode

import base64

### MAIN PROGRAM ###

def main():
    encoded = []
    print('Reading contents from file...')
    with open('c8_file.txt', 'rt') as f:
        for l in f:
            encoded.append(l[:-1])
    encoded = [bytes(e, 'utf_8') for e in encoded]
    encoded = [base64.b16decode(e.upper()) for e in encoded]
    print('Done')

    print('Finding cipher text with repeated blocks of same text...')
    k = 0
    for e in encoded:
        for i in range(0, len(e), 16):
            for j in range(i+16, len(e)+1, 16):
                if e[i:i+16] == e[j:j+16]:
                    print(k)
        k+=1
    
    print('So, line 133(1-indexed) is the encoded string')

if __name__ == '__main__':
    main()
