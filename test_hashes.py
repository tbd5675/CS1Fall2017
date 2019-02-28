"""
A simple program that provides a test that may be used to validate that a
hashing function consistently produces the same hashcode when it is called
many times with the same key.

author: Bobby St. Jacques

date: 12/01/2017
"""


def test_hash_func(hash_func):
    """
    Tests a hashing function to verify that it produces the same hashcode when
    the same keys are used multiple times.
    :param hash_func: The hash function being tested.
    :param name: The name of the hash function (used for output).
    :return: None
    """

    # this is used to get the name of the function being tested
    name = hash_func.__name__

    # store 100 keys in a Python list
    keys = []
    file = open("keys.txt")
    for i in range(10):
        key = file.readline().strip()
        keys += [key]
    file.close()

    '''
    Use the provided hash function to hash each of the keys and store the
    results in a Python dictionary
    '''
    results = {}
    for key in keys:
        hashcode = hash_func(key)
        results[key] = hashcode
    file.close()

    '''
    For each key, verify that the provided hash function returns the same
    hashcode each time that it is called.
    '''
    success = True
    for i in range(10):
        for key in results:
            old_hashcode = results[key]
            new_hashcode = hash_func(key)
            if old_hashcode != new_hashcode:
                print(" ", name, "failed with key", key, "expected",
                      old_hashcode, "but got", new_hashcode)
                success = False
                break

    if success:
        print(" ", name, "passed all tests!")
    else:
        print(" ", name, "failed at least one test (see above)")