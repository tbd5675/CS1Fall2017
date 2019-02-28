"""
Tate Dyer
HW 10
"""

from link_sort import *

def main():
    file=input("Enter file name: ")
    if file=="":
        quit()
    else:
        lns= read_file(file)
        print("unsorted sequence:", lns)
        sorted_lns=link_sort(lns)
        print("sorted sequence:", sorted_lns)
        print("pretty printed original:",  pretty_print(lns))
        print("pretty printed sorted:", pretty_print(sorted_lns))

main()