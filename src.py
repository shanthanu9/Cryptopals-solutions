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


def expected_freq_of_english():
    # returns the expected frequency of english
    # alphabets [a-z] between 0 and 1
    
    return [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]


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


### MAIN PROGRAM ###

def main():
    s = b'\x00'
    print(score_plaintext(s))


if __name__ == '__main__':
    main()

