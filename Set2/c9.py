#Implement PKCS#7 padding

### FUNCTIONS ###

def PKCS_pad(s, block_size):
    # pad string s to block_size

    pad = block_size-len(s)%block_size
    l = [i for i in s]
    for i in range(0, pad):
        l.append(pad)

    return bytes(l)

### MAIN PROGRAM ###

def main():
    block_size = 20
    plaintext = b'YELLOW SUBMARINE'
    print(PKCS_pad(plaintext, block_size))

if __name__ == '__main__':
    main()
