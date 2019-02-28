"""
Tate Dyer
HW 6
"""

def match(string1, string2):
    """
    Identifies and returns the length of a longest
    common consecutive substring shared
    by the two input strings.
    :param string1: The first string.
    :param string2: The second string.
    :return: length of a longest shared consecutive string.
    """

    best_length = 0
    # for all possible string1 start points
    for idx1 in range(len(string1)-1):
        # for all possible string2 start points
        for idx2 in range(len(string2)-1):
            # check if these characters match
            if string1[idx1] == string2[idx2]:
                this_match_count = 1
                # see how long the match continues

                while (idx1 + this_match_count<len(string1) and
                        idx2 + this_match_count<len(string2)) and\
                        string1[idx1 + this_match_count] == \
                        string2[idx2 + this_match_count]:
                    this_match_count += 1
                # compare to best so far
                if this_match_count > best_length:
                    best_length = this_match_count

    # now return the result
    return best_length

def main():
    print(match("established", "ballistic"))
    print(match("yellow", "hello"))
    print(match("bugspray", "ladybug"))
    print(match("what", "rattler"))
    print(match("dad", "bad"))
    print(match("deadpool", "swimming"))
    print(match("lacrosse", "crowd"))

main()