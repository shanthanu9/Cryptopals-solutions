#Convert hex to base 64

import base64

#input hex string, b'' represents a byte object
HEX = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
B64 = base64.b64encode(base64.b16decode(HEX.upper()))           #Note HEX.upper()

assert(B64 == b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')
