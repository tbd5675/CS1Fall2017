"""
Tate Dyer
Lab 10
"""
from rit_lib import *

Trie = struct_type( "Trie", ((NoneType, 'Trie'), "left"), ( object, "value"), ((NoneType, 'Trie'), "right"))

def insert(T,x,c=0):
    if T.value=="":
        side=x[c]
        if side==0:
            insert(T.left,x,c+1)
        else:
            insert(T.right,x,c+1)
    elif T.value is None:
        T.value=x
        return True
    else: #if value is a leaf
        while x[c] == T.value[c]:
            c+=1
        if x[c]==0:
            T.left.value= Trie(None, T.value, None)
            T.right.value= Trie(None, x, None)
        else:
            T.left = Trie(None, x, None)
            T.right = Trie(None, T.value, None)
        T.value=""
        return True

def trie_to_list(trie):
    lst=[]


def largest(trie):

    if trie.value=="" and trie.right is None:
        largest(trie.left)
    elif trie.right is None:
        return trie.value
    elif trie.value!="" and trie.right is None:
        return trie.value
    else:
        largest(trie.right)

def smallest(trie):
    if trie.left is None:
        return trie.value
    else:
        smallest(trie.left)

def search(trie, st, c=0):
    if trie is None:
        return False
    else:
        if st == trie.value:
            return True
        elif st[c]==0:
            return search(trie.left, st, c+1)
        elif st[c]==1:
            return search(trie.right, st, c+1)

def size(trie, acc=0):
    if trie.value=="":
        size(trie.right)
        size(trie.left)
    elif trie.value is None:
        pass
    else:
        size(trie.right, acc+1)
        size(trie.left, acc+1)
    return acc

def height(trie):
    if trie.left is None:
        return 0
    else:
        return 1+height(trie.left)