# Cryptopals-solutions

Solutions to cryptopals challenges. All code here is written in python 3.6. [src.py](./src.py) contains functions commonly used across all challenges.

TO run a particular challenge 'x' in set 'y', run the following command on the terminal

> $ python3 Setx/cy.py

## Set 1 : Basics

1. [Convert hex to base64](./Set1/c1.py)  
    A simple problem. I used python base64 library to solve this.

2. [Fixed XOR](./Set1/c2.py)  
    Simple problem. But I used python bytes object to solve this. I used bytes.fromhex() method to convert unicode representation of a hex string into a hex equivalent string. Also used bytes.hex() to do the reverse of the above process.   
This makes life easier because otherwise I would have to write lot of messy for loops.

3. [Single-byte XOR cipher](./Set1/c3.py)  
    Nice one. I brute forced all possible characters to xor with. For "scoring" based on frequncy, I used chi-squared statistic technique. 

4. [Detect single-character XOR](./Set1/c4.py)  
    This was a very interesting one. I first brute forced through all possible solutions. Then I tried to score each decoding a looking at strings with low scores (similar to c3). But there were a lot of strings to consider. So, I considered only strings with high frequency of alphabets (more than 60%) which reduced the count to 5 strings.

5. [Implement repeating-key XOR](./Set1/c5.py)  
    Implementaion question. I wrote a function to perform repeated xor on a string.

6. [Break repeating-key XOR](./Set1/c6.py)  
    Oof this one was tough.

    First, I had to convert the base64 string to hex form.

    The initial task to implement the hamming distance function. The catch here is to compare the 'bits', not just the characters. I have defined my hamming distance in [src.py](./src.py). 

     Next I had to guess the key size. This was to be done by finding the normalised hamming distance for different keysizes. The idea is the one with the least value is the probable key size. Initially, I made the mistake of using just two strings (i.e, the initial first two), which gave me erraneous results. Rectifying this error,  I averaged over the entire encoded string which gave me a accurate value for keysize. In the challenge it is suggested to consider the top 2-3 values. Turns out the lowest value itself is the corret key size.

    Next I had to figure out the key. For this, first I broke the encoded string into blocks of keysize. Then I transposed these blocks to get a block which is first byte of every block, second byte, third byte and so on. Then I cracked each block as if it was encoded by single key xor. (Here we could reuse code from challenge 3 Set 1)
   
    Then I concatenated the results obtained for each block and obtained the key. Since I used chi mean squared statistic, the resulting key I obtained was correct in all positions except for one. I figured out the correct key by some (easy) trial and error.

7. [AES in ECB mode](./Set1/c7.py)  
    I used cryptodome library to solve this one. Very simple one. 

    First converted to bytes from base64. Then used the key to decrypt the cipher text using Crypto.Cipher library.

8. [Detect AES in ECB mode](./Set1/c8.py)  
    The problem was to detect the line in the given file encoded AES in ECB mode. I tried to find the line by checking each line if any block of 16 bytes repeated. And it did for one of them. 

    Initially all lines in the file were hex encoded which I had to decode.


