# library of commonly used functions in the challenges

# NOTE: For all functions, plaintext inputs must be a bytes object

import math

### FUNCTIONS ###

def frequency(s):
    # returns list of frequencies of
    # characters of s in range [0-255] in utf-8

    size = 256
    freq = [0]*size
    for i in s:
        freq[i] += 1

    return freq


def frequency_of_alpha(s):
    # returns only frequency of alphabets [a-z] in s
    # doesn't diffrentiate between lower and upper case
    
    return frequency(s.lower())[97:123]

def frequency_of_all_alpha(s):
    # returns only frequency of [a-z]+space in s
    # doesn't diffrenciate between lower and upper

    l = frequency(s.lower())
    return l[97:123]+[l[ord(' ')]]

def expected_freq_of_space():
    # simply retunrs the average frequency of space
    return [0.13000]

def expected_freq_of_english():
    # returns the expected frequency of english
    # alphabets [a-z] between 0 and 1
    
    return [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]


def expected_freq_of_all_alpha():
    # returns expected frequency of english
    # [a-z] and ending with space
    return expected_freq_of_english() + expected_freq_of_space()

def score_plaintext_with_sum(s):
    # compares the frequency of letters in s with english letters
    # returns the sum of character frequencis
    # simple but effective metric
    # NOTE: the metric is normalised
    
    expected = expected_freq_of_all_alpha()
    count = frequency_of_all_alpha(s)

    return sum([e*c for e,c in zip(expected, count)])/len(s)


def score_plaintext(s):
    # compares the frequency of letters in s with english letters
    # uses chi squared statistic technique
    # returns a positive score for s
    # if frequency distribution of s is similar to english,
    # then a low score is returned, else a high score

    expected = expected_freq_of_english()
    count = frequency_of_alpha(s)
    return chi(count, expected)


def chi(count, expected):
    # counts: counts of symbols(like alphabets) in list1
    # expected: probability distribution of list2
    # returns chi-squared statistic of the two lists
    # don't bother to use this in code, mostly a helper function
    # in this module :)

    total_count = sum(count)
    if total_count == 0:
        return math.inf

    return sum([((c-total_count*p)*(c-total_count*p))/(total_count*p) for c,p in zip(count, expected)])

def percentage_alpha(s):
    # returns the percentage of characters in s
    # returns a number between 0 to 100

    count = 0
    for b in s:
        if chr(b).isalpha():
            count += 1
    return count/len(s)*100

def differing_bits(a,b):
    # given two bytes a and b(integers)
    # returns the number of differing bytes
    # helper method

    bits = 0
    for i in range(0,8):
        if (1<<i)&a != (1<<i)&b:
            bits += 1

    return bits

def hamming_distance(a, b):
    # returns number of differing bits between a and b
    # a and b must be of same lenght

    if len(a) != len(b):
        raise ValueError('Arguements to hamming_distance must have same length')
    
    bits = 0
    for i,j in zip(a,b):
        bits += differing_bits(i,j)    

    return bits

def range_alphanum():
    # return a list with ascii values of digits and
    # English alphabets

    l = []
    for i in range(48,58):
        l.append(i)
    #for i in range(65,91):
    #    l.append(i)
    for i in range(97,123):
        l.append(i)
    
    return bytes(l)

def percentage_gibberish(s):
    # returns percentage of non English characters
    
    count = 0
    for c in s:
        if c < 32 or c > 126:
            count += 1

    return count/len(s) * 100


### MAIN PROGRAM ###

def main():
    a = b'this is a test'
    b = b'wokka wokka!!!'
    print(hamming_distance(a,b))
    print(score_plaintext_with_sum(b'  23j jhfl'))

if __name__ == '__main__':
    main()

