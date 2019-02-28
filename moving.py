"""
Tate Dyer
Lab 7
"""
from rit_lib import *

Box= struct_type("Box", (int, "size"))
Item= struct_type("Item", (str, "name"), (int,"size"))

def make_box(size):
    """
    creates a box based on a size given from the file
    :param size: size of a box
    :return: the box as a structure
    """
    box=Box(size)
    return box

def make_item(name, size):
    """
    creates a item based on its name and size given from the file
    :param name: name of an item
    :param size: size of an item
    :return: the item as a structure
    """
    item=Item(name,size)
    return item

def moving(file):
    """
    takes in a file and breaks it apart into structures of boxes and items
    :param file: file input
    :return: list of boxes and list of items
    """
    count=0
    fd=open(file)
    listB=[]
    listI=[]
    for line in fd:
        if count==0:
            boxes=line.split()
            count+=1
            for i in boxes:
                listB.append(make_box(int(i)))
        else:
            (namei, sizei)=line.split()
            listI.append(make_item(namei, int(sizei)))
    fd.close
    return listB, listI

def roomiest(box_list, item_list):
    """
    sorts items by decreasing weight, iterates through the items and then for each item identifies
    the box with the greatest remaining weight that can support the item and places the item in the box.
    continues until all items have been considered and either placed in a box or left out
    :param box_list: list of box structures
    :param item_list: list of item structures
    :return:
    """
    item_sorted_list=sorted(item_list, key=lambda test: test.size, reverse=True)
    for i in item_sorted_list:
        high=0
        p=0
        hp=0
        lb=0
        for b in box_list:
            if b.size>high:
                if b.size>=i.size:
                    high=b.size
                    hp=p
            p+=1
        if high==0:
            print(i.name, "of weight", i.size, "got left behind.")
            lb=1
        else:
            print(i.name, "of weight", i.size, "was packed into Box", (box_list.index(Box(high)))+1)
            box_list[hp].size-=i.size
    if lb==0:
        print("All items were successfully packed into boxes!")
    else:
        print("Unable to pack all items!")

def tightest_fit(box_list, item_list):
    """
    sorts items by decreasing weight, iterates through the items and then for each item identifies
    the box with the least remaining weight that can support the item and places the item in the box.
    continues until all items have been considered and either placed in a box or left out
    :param box_list: list of box structures
    :param item_list: list of item structures
    :return:
    """
    item_sorted_list = sorted(item_list, key=lambda test: test.size, reverse=True)
    for i in item_sorted_list:
        low=10000000
        p=0
        hp=0
        lb=0
        for b in box_list:
            if b.size<low:
                if b.size>=i.size:
                    low=b.size
                    hp=p
            p+=1
        if low==10000000:
            print(i.name, "of weight", i.size, "got left behind.")
            lb=1
        else:
            print(i.name, "of weight", i.size, "was packed into Box", (box_list.index(Box(low)))+1)
            box_list[hp].size-=i.size
    if lb==0:
        print("All items were successfully packed into boxes!")
    else:
        print("Unable to pack all items!")

def one_box_at_a_time(box_list, item_list):
    """
    sorts items by decreasing weight, iterates through each box by filling them one at a time.
    If room for item in box then puts it in
    :param box_list: list of box structures
    :param item_list: list of list structures
    :return:
    """
    item_sorted_list = sorted(item_list, key=lambda test: test.size, reverse=True)
    bp=0
    for b in box_list:
        for i in item_sorted_list:
            if b.size>=i.size:
                print(i.name, "of weight", i.size, "was packed into Box", (box_list.index(b)) + 1)
                box_list[bp].size -= i.size
                item_sorted_list.remove(i)
        bp+=1
    if len(item_sorted_list)==0:
        print("All items were successfully packed into boxes!")
    else:
        for i in item_sorted_list:
            print(i.name, "of weight", i.size, "got left behind.")
        print("Unable to pack all items!")

def main():
    filename=input("Enter file name: ")
    (box,item)=moving(filename)
    print("Results from Greedy Strategy 1")
    roomiest(box,item)
    print("")
    (box, item) = moving(filename)
    print("Results from Greedy Strategy 2")
    tightest_fit(box,item)
    print("")
    (box, item) = moving(filename)
    print("Results from Greedy Strategy 3")
    one_box_at_a_time(box,item)

main()