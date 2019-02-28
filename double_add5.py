"""
Tate Dyer
HW 4
"""
import math

"""
given a number to start at multiplies it by 2 and adds 5
a specified count times through recursion
"""
def print_sequence_rec(start, count):
    if count<0:
        pass
    else:
        print (start)
        print_sequence_rec(start * 2 + 5, count - 1)

"""
given a number to start at multiplies it by 2 and adds 5
a specified count times through iteration
"""
def print_sequence_iter(start, count):
    while count>=0:
        print(start)
        start=start*2+5
        count=count-1

"""

"""
def find_start_forward(goal, count):
    startinitial=0
    start=0
    while(start<=goal):
        countinitial = count
        startinitial=startinitial+1
        start=startinitial
        while countinitial > 0:
            start = start * 2 + 5
            countinitial = countinitial - 1
    return startinitial

"""
test function for find_start_forward
"""
def test_find_start_forward():
    print("find_start_forward tests")
    print(find_start_forward(100, 3))
    print("")
    print(find_start_forward(100, 1))
    print("")
    print(find_start_forward(1000, 3))
    print("")

"""
given a number determines what the start value was
that was multiplied by 2 and increase by 5 count times 
to reach the number through recursion
"""
def find_back_limit_rec(nbr, count):
    if count<=0:
        if nbr<0:
            return 0
        return nbr+5
    else:
        return find_back_limit_rec((nbr//2)-5, count-1)

"""
test function for find_back_limit_rec
"""
def test_find_back_limit_rec():
    print("find_back_limit_rec tests")
    print(find_back_limit_rec(1000,3))
    print("")
    print(find_back_limit_rec(100, 2))
    print("")
    print(find_back_limit_rec(350, 5))
    print("")

"""
given a number determines what the start value was
that was multiplied by 2 and increase by 5 count times 
to reach the number through iteration
"""
def find_back_limit_iter(nbr, count):
    while count>0:
        nbr=(nbr//2)-5
        count=count-1
    if nbr<0:
        return 0
    return nbr+5

"""
test function for find_back_limit_iter
"""
def test_find_back_limit_iter():
    print("find_back_limit_iter tests")
    print(find_back_limit_iter(1003,3))
    print("")
    print(find_back_limit_iter(4194299, 3))
    print("")
    print(find_back_limit_iter(10, 3))


def main():
    print("print_sequence_rec tests")
    print_sequence_rec(1,2)
    print(" ")
    print_sequence_rec(0, -1)
    print(" ")
    print_sequence_rec(0, 0)
    print(" ")
    print_sequence_rec(1, 0)
    print(" ")
    print("print_sequence_iter tests")
    print_sequence_iter(2,5)
    print(" ")
    print_sequence_iter(121,3)
    print(" ")
    print_sequence_iter(1, 1)
    print(" ")
    print_sequence_iter(9, 3)
    print(" ")
    test_find_start_forward()
    print(" ")
    test_find_back_limit_rec()
    print(" ")
    test_find_back_limit_iter()

main()