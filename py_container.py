'''
array
'''
ls = [1, 2, 3]

'''
栈的使用.
'''
class stack:
    def __init__(self):
        ls = []

    def peek(self):
        return ls[len(ls) -1]

    def pop(self):
        return ls.pop()

    def isEmpty(self):
        return len(ls) == 0

    def size(self):
        return len(ls)

'''
队列的使用.
'''
from collections import deque
def use_queue():
    deque.append()


'''
堆的使用.
'''


def use_heap():
    pass


'''
集合的使用.
'''


def use_set():
    st = set()  # create an empty set
    st = {1, 2, 3}  # create a set with initialisation
    st.add(1)  # insert item into the set
    st.remove(2)  # remove an item
    2 in st  # find an item

    print(st)
