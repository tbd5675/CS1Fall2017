"""
Tate Dyer
HW 6
"""

def caesar(original, codeword):
    """
    Tests whether the provided codeword string
    represents a valid encoding of the original
    string using a Caesar cipher.
    Pre-condition:  both the codeword and original
    are strings containing only capitalized English
    letters.
    Pre-condition:  neither the codeword nor the
    original string is the empty string.
    :param original: The original string.
    :param codeword: The encoded string.
    :return: Integer in the range 0-25 if the codeword
    represents a valid encoding of the original
    string using a Caesar cipher.
    Returns -1 otherwise.
    """

    # Use built-in ord() function to get ASCII
    # integer value associated with A-Z.
    # A has value 65, B is 66, ..., Z is 90.

    # Get shift for first character.  All characters must
    # have identical shift for it to be a valid Caesar shift.
    shift = (ord(codeword[0]) - ord(original[0]))%26 #added modulus 26 becasue always creates an integer 0 to 25 to be used

    for idx in range(len(codeword)):
        if (ord(codeword[idx]) - ord(original[idx]))%26 != shift: #added modulus 26 again with same function
            return -1

    return shift

def main():
    print(caesar("ABC", "JKL"))
    print(caesar("VERY", "AJWD"))
    print(caesar("POOL", "ZYYV"))
    print(caesar("DINOSAUR", "TREDHOCH"))
    print(caesar("WHAT", "BMFY"))
    print(caesar("GETTING", "DKLLTY"))

main()