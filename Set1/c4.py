#Detect single-character XOR

import sys
sys.path.insert(0, '../')

import src
import c3
from math import inf

### FUNCTIONS ###

def is_alpha(s):
    #check if unicode value of all characters is less than 128
    for b in s:
        if b > 127:
            return False
    return True

### MAIN FUNCTION ###

def main():
    encoded = []
    print("Loading contents from file...")
    with open('c4_file.txt','rt') as f:
        for line in f:
            encoded.append(bytes.fromhex(line[:-1]))
    print("Done loading.")

    decoded = []
    print("Brute forcing all possible combinations...")
    for e in encoded:
        for i in range(0, 256):
            decoded.append(c3.xor_string_with_char(e, i))
            #if(is_alpha(decoded[-1])):
            #    print(decoded[-1])
    print("Done.")
    
    print("Finding probable decoded strings...")
    l = []
    for d in decoded:
        if is_alpha(d):
            score = src.score_plaintext(d)   
            #print(score,":", d)
            if score < 50 and src.percentage_alpha(d) > 60:
                l.append([score, d.decode('utf_8', 'ignore')])
    print("Done.")

    print("Generating probable decoded strings...")
    l.sort()
    for i,j in l:
        print(i,":",j)
    print("Done!") 
     

if __name__ == '__main__':
    main()
