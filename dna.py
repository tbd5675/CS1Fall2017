"""
Tate Dyer
Lab 8
"""

from linked_code import *

def convert_to_nodes(dna_string):
    """
    creates a linked node data set where each character of a string is represented as a node
    :param dna_string: string to be made into a node
    :return: linked node data structure representing each character of a given string
    """
    if dna_string=="":
        return None
    else:
        return Node(dna_string[0], convert_to_nodes(dna_string[1:]))

def convert_to_string(dna_seq):
    """
    converts given sequence to a string
    :param dna_seq: a linked sequence with data nodes representing a DNA sequence
    :return: string of the sequence
    """
    copy_dna_seq=dna_seq
    dna_str=""
    while copy_dna_seq is not None:
        dna_str=dna_str+copy_dna_seq.value
        copy_dna_seq=copy_dna_seq.rest
    return dna_str

def is_match(dna_seq1, dna_seq2):
    """
    goes element by element to check if the two sequences are identical or not
    :param dna_seq1: first linked sequence with data nodes representing a DNA sequence
    :param dna_seq2: second linked sequence with data nodes representing a DNA sequence
    :return: boolean True or False
    """
    if dna_seq1 is None and dna_seq2 is None:
        return True
    elif dna_seq1 is None or dna_seq2 is None:
        return False
    elif dna_seq1.value==dna_seq2.value:
        return is_match(dna_seq1.rest, dna_seq2.rest)
    else:
        return False

def is_pairing(dna_seq1, dna_seq2):
    """

    :param dna_seq1: first linked sequence with data nodes representing a DNA sequence
    :param dna_seq2: second linked sequence with data nodes representing a DNA sequence
    :return: Boolean True or False
    """
    if lengthIter(dna_seq1)!=lengthIter(dna_seq2):
        return False
    if dna_seq1 is None and dna_seq2 is None:
        return True
    else:
        if(dna_seq1.value == "A" and dna_seq2.value=="T") or (dna_seq1.value == "T" and dna_seq2.value=="A"):
            return is_pairing(dna_seq1.rest, dna_seq2.rest)
        elif(dna_seq1.value == "G" and dna_seq2.value=="C") or (dna_seq1.value == "C" and dna_seq2.value=="G"):
            return is_pairing(dna_seq1.rest, dna_seq2.rest)
        else:
            return False

def is_palindrome(dna_seq):
    """
    compares the reverse of the sequence to the normal one to see if they are the same
    :param dna_seq: a linked sequence with data nodes representing a DNA sequence
    :return: boolean True or False
    """
    copy_dna_seq=dna_seq
    reverse_dna_seq=reverseIter(copy_dna_seq)
    while copy_dna_seq is not None and reverse_dna_seq is not None:
        if copy_dna_seq.value == reverse_dna_seq.value:
            copy_dna_seq=copy_dna_seq.rest
            reverse_dna_seq=reverse_dna_seq.rest
        else:
            return False
    if copy_dna_seq is None and reverse_dna_seq is None:
        return True
    elif copy_dna_seq is None or reverse_dna_seq is None:
        return False

def substitution(dna_seq1, idx, base):
    """
    removes the item at the given index and then inserts the given value into its place
    :param dna_seq1: linked sequence
    :param idx: index to be substituted at
    :param base: value to be substituted for the item at the given index
    :return: sequence with new value inserted
    """
    copy_dna_seq=dna_seq1
    if lengthIter(dna_seq1)<idx:
        raise IndexError("index out of bounds")
    else:
        copy_dna_seq=removeAt(idx, copy_dna_seq)
        copy_dna_seq=insertAt(idx, base, copy_dna_seq)
    return copy_dna_seq

def insertion(dna_seq1, dna_seq2, idx):
    """
    inserts dna_seq2 at the index of dna_seq1
    :param dna_seq1: first linked sequence with data nodes representing a DNA sequence
    :param dna_seq2: second linked sequence with data nodes representing a DNA sequence
    :param idx: index before which the insertion occurs
    :return: a new linked sequence after the insertion
    """
    if idx==1:
        return Node(dna_seq1.value, cat(dna_seq2, dna_seq1.rest))
    elif dna_seq1 is None and idx>1:
        raise IndexError("invalid insertion index")
    elif idx==0:
        return cat(dna_seq2, dna_seq1)
    else:
        return Node(dna_seq1.value, insertion(dna_seq1.rest, dna_seq2, idx-1))

def deletion(dna_seq, idx, segment_size):
    """
    finds the starting index and begins deleting until reaches the segment size number of deletions
    :param dna_seq: a linked sequence with data nodes representing a DNA sequence
    :param idx: the index at which deletion begins
    :param segment_size: number of elements to be deleted
    :return: linked sequence with the values from one index to another deleted
    """
    count=0
    copy_dna_seq=dna_seq
    copy2_dna_seq = dna_seq
    if segment_size>0 and lengthIter(dna_seq)<=idx:
        raise IndexError("index out of bounds")
    else:
        while copy_dna_seq is not None:
            if count==idx:
                while segment_size>=1:
                        copy2_dna_seq=remove(copy_dna_seq.value, copy2_dna_seq)
                        copy_dna_seq = copy_dna_seq.rest
                        segment_size-=1
                count+=1
            else:
                copy_dna_seq = copy_dna_seq.rest
                count+=1
        return copy2_dna_seq


def duplication(dna_seq, idx, segment_size):
    """
    duplicates from index number of spaces after and inserts the duplication after the items duplicated into a new sequence
    :param dna_seq: a linked sequence with data nodes representing a DNA sequence
    :param idx: index to start the duplicating
    :param segment_size: number of items after index to add to a new sequence
    :return: new linked sequence
    """
    count = 0
    copy_dna_seq = dna_seq
    new_dna_seq= None
    dup_seq= None
    after_seq=None
    if segment_size>0 and lengthIter(dna_seq)<=idx:
        raise IndexError("index out of bounds")
    else:
        while copy_dna_seq is not None:
            if count<idx:
                new_dna_seq = Node(copy_dna_seq.value, new_dna_seq)
                copy_dna_seq = copy_dna_seq.rest
                count += 1
            elif count == idx:
                while segment_size >= 1:
                    new_dna_seq = Node(copy_dna_seq.value, new_dna_seq)
                    dup_seq=Node(copy_dna_seq.value, dup_seq)
                    copy_dna_seq=copy_dna_seq.rest
                    segment_size -= 1
                count+=1
            else:
                after_seq = Node(copy_dna_seq.value, after_seq)
                copy_dna_seq = copy_dna_seq.rest
                count += 1
        new_dna_seq=reverseIter(new_dna_seq)
        dup_seq=reverseIter(dup_seq)
        new_dna_seq = cat(new_dna_seq, dup_seq)
        after_seq=reverseIter(after_seq)
        new_dna_seq=cat(new_dna_seq,after_seq)
        return new_dna_seq