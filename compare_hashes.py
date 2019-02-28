"""
Tate Dyer
HW 12
"""

from rit_lib import *
from hashtable import *
from test_hashes import *
from time import *
import math


def put_count(hTable, key, value):
    """
    put: HashTable(K, V) K V -> Boolean

    Using the given hash table, set the given key to the
    given value. If the key already exists, the given value
    will replace the previous one already in the table.
    If the table is full, an Exception is raised.
    counts num of collisions
    """
    count=0
    index = int(hTable.hash_func(key) % hTable.capacity)
    startIndex = index  # We must make sure we don't go in circles.
    while hTable.table[index] != None and hTable.table[index].key != key:
        index = (index + 1) % hTable.capacity
        count+=1
        if index == startIndex:
            raise Exception("Hash table is full.")
    if hTable.table[index] == None:
        hTable.table[index] = Entry(key, value)
        hTable.size += 1
    else:
        hTable.table[index].value = value
    return count

def always_hashes_to_zero(key):
    return 0

def evaluate_worst(lst):
    print("Evaluating always_hashes_to_zero")
    test_hash_func(always_hashes_to_zero)
    h = createHashTable(always_hashes_to_zero,len(lst))
    total=0
    start=time()
    for key in lst:
        total+=put_count(h, key, key)
    end=time()
    t=end-start
    average=total/len(lst)
    print("Inserted", len(lst), "items into the hashtable in ", t," seconds")
    print("Average length of linear search:", average)

def add_ordianl_values(key):
    return ord(key[0])+ord(key[1])+ord(key[2])

def evaluate_add(lst):
    print("Evaluating add_ordianl_values")
    test_hash_func(add_ordianl_values)
    h = createHashTable(always_hashes_to_zero,len(lst))
    total = 0
    start = time()
    for key in lst:
        total += put_count(h, key, key)
    end = time()
    t = end - start
    average = total / len(lst)
    print("Inserted", len(lst), "items into the hashtable in ", t, " seconds")
    print("Average length of linear search:", average)

def pow_ordianl_values(key):
    return math.pow(ord(key[0]),ord(key[0]))+math.pow(ord(key[1]),ord(key[1]))+math.pow(ord(key[2]),ord(key[2]))

def evaluate_pow(lst):
    print("Evaluating pow_ordianl_values")
    test_hash_func(pow_ordianl_values)
    h = createHashTable(always_hashes_to_zero,len(lst))
    total = 0
    start = time()
    for key in lst:
        total += put_count(h, key, key)
    end = time()
    t = end - start
    average = total / len(lst)
    print("Inserted", len(lst), "items into the hashtable in ", t, " seconds")
    print("Average length of linear search:", average)

def good_hash_func(key):
    return ord(key[0])*math.pow(31,2)+ord(key[1])*31+ord(key[2])

def evaluate_good(lst):
    print("Evaluating good_hash_func")
    test_hash_func(good_hash_func)
    h = createHashTable(always_hashes_to_zero,len(lst))
    total = 0
    start = time()
    for key in lst:
        total += put_count(h, key, key)
    end = time()
    t = end - start
    average = total / len(lst)
    print("Inserted", len(lst), "items into the hashtable in ", t, " seconds")
    print("Average length of linear search:", average)

def my_hash_func(key):
    return math.pow(ord(key[0]),3)+math.pow(ord(key[1]),2)+math.pow(ord(key[2]),1)

def evaluate_own(lst):
    print("Evaluating my_hash_func")
    test_hash_func(my_hash_func)
    h = createHashTable(always_hashes_to_zero,len(lst))
    total = 0
    start = time()
    for key in lst:
        total += put_count(h, key, key)
    end = time()
    t = end - start
    average = total / len(lst)
    print("Inserted", len(lst), "items into the hashtable in ", t, " seconds")
    print("Average length of linear search:", average)

def main():
    file=input("Enter the name of the file containing the keys: ")
    input("Enter the capacity of the hash table: ")
    with open(file) as f:
        lst=[]
        for line in f:
            lst+=line.strip().split(",") #how to split every 3 characters? realized no commas
        print(lst)
    evaluate_worst(lst)
    evaluate_add(lst)
    evaluate_pow(lst)
    evaluate_good(lst)
    evaluate_own(lst)

if __name__ == '__main__':
    main()