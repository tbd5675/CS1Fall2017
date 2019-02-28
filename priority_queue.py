"""
Tate Dyer
HW 7

1.O(1)
2.O(N*log(N))
3.O(N)
4.O(1)
5.It is worse because the complexity to find where the index the item is to be placed in is higher than any actions
complexity within the built in Python function.

"""
def binary_search(queue, item, start, end):
    """
    Function that uses binary search to find index that the item is supposed to go
    :param queue: the priority queue
    :param item: the number to be added to the queue
    :param start: the start position of computing midpoint
    :param end: he end position of computing midpoint
    :return: index
    """
    if start > end:
        return start
    mid_index = (start + end) // 2
    if item == queue[mid_index]:
        return mid_index
    elif start==end-1:
        return end
    elif queue[mid_index] < item:
        return binary_search(queue, item, start, mid_index - 1)
    else:
        return binary_search(queue, item, mid_index + 1, end)


def enqueue(queue, item):
    """
    adds item in the correct place within the priority queue by calling binary search
    :param queue: the priority queue
    :param item: value to be added into the queue
    :return: new priority queue with added item
    """
    if len(queue)==0:
        queue=[item]
    else:
        id=binary_search(queue, item, 0, (len(queue)-1))
        queue=queue+[None]
        for i in range(len(queue)-2, id):
            queue[i+1]=queue[i]
            queue[i]=[None]
        queue[id]=item
    return queue

def dequeue(queue):
    """
    removes the highest priority item in queue
    :param queue: the priority queue
    :return: the item removed
    """
    return queue.pop()

def test_enqueue():
    """
    tests the enqueue function by adding items and printing the final list when theyve all been added
    :return:
    """
    pq = list()
    pq=enqueue(pq, 7)
    pq=enqueue(pq, 4)
    pq=enqueue(pq, 3)
    pq=enqueue(pq, 8)
    pq=enqueue(pq, 2)
    print(pq)

def test_dequeue():
    """
    tests the dequeue function by having a list and calling dequeue and then printing the list after
    :return:
    """
    pq=[8,6,3,1]
    pq=dequeue(pq)
    print(pq)

def test():
    """
    tests both functions working together
    :return:
    """
    pq = list()
    pq=enqueue(pq, 5)
    pq=enqueue(pq, 1)
    pq=enqueue(pq, 3)
    print("Highest priority item is ", dequeue(pq))
    print("Next highest priority task is ", dequeue(pq))

def main():
    test_enqueue()
    test_dequeue()
    test()

main()
