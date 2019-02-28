"""
Tate Dyer
HW 10
"""

from linked_code import *

def link_sort(lns):
    """
    takes a linked Node sequence, implements the selection sort algorithm
    :param lns: linked Node sequence
    :return: the sorted sequence in ascending order
    """
    sorted_lns=None
    unsorted_lns=lns
    while unsorted_lns is not None:
        little=find_min_value(unsorted_lns, unsorted_lns.value)
        if sorted_lns is None:
            sorted_lns=Node(little,None)
        else:
            insertAt(0, little, sorted_lns)
        remove(little, unsorted_lns)
    sorted_lns=reverseIter(sorted_lns)
    return sorted_lns

def find_min_value(seq, small):
    """
    finds the smalled value in a linked sequence
    :param seq: linked Node sequence
    :param small: smallest value
    :return: smallest value
    """
    if seq == None:
        return small
    else:
        current = seq.value
        if current<small:
            small=current
        return find_min_value(seq.rest, small)

def pretty_print(lns):
    """
    returns the linked sequence as a list
    :param lns: linked Node sequence
    :return: list of the values in the linked Node sequence
    """
    copy_lns=lns
    lst=[]
    if lns is None:
        pass
    else:
        item=lns.value
        while item is not None:
            lst.append(lns.head)
            item=lns.rest.value
    return lst

def read_file(filename):
    """
    given a file opens it, and goes line by line adding values to a linked Node sequence
    :param filename: input file
    :return: linked Node sequence
    """
    lns=None
    with open(filename) as f:
        idx=0
        for line in f:
            lns=cat(lns, Node(int(line.strip()), None))
    return lns
