# Cryptopals-solutions

Solutions to cryptopals challenges. All code here is written in python 3.6. [src.py](./src.py) contains functions commonly used across all challenges.

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