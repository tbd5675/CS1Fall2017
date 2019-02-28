"""
Tate Dyer
Lab 6
"""

def quickSort ( L ):
    if L == []:
        return []
    else:
        pivot=L[0]
        (less, same, more) = partition (pivot, L)
    return quickSort(less)+same+quickSort(more)

def partition ( pivot , L ):
    (less, same, more) = ([], [], [])
    for i in L:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)
        else:
            same.append (i)
    return (less, same, more)

def best_location(list):
    location=0
    sorted_list=quickSort(list)
    if len(sorted_list)%2==1:
        location=sorted_list[len(sorted_list)//2]
    else:
        top=len(sorted_list)//2
        bot=(top-1)
        location=(sorted_list[top]+sorted_list[bot])//2
    return location

def sum_of_distances(list, loc):
    total=0
    for i in list:
        total=total+(abs(loc-i))
    return total

def split_values(file):
    locations=[]
    for line in file:
        values=line.split()
        num=int(values[1])
        locations.append(num)

def main():
    pass