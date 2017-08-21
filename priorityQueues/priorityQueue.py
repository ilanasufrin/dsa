"""
This class is an implementation of a (minimum) priority queue using an array backing. 
It holds on to data as a list of tuples: (data, priority)

"""
from collections import deque

class PriorityQueue():

    def __init__(self):
        self.queue = []

    """Push item onto heap, maintaining the heap invariant afterwards."""
    def push(self, item):
        if type(item) != tuple or type(item[1]) != int:
            raise ValueError('Item to insert must be a tuple of (data, int(priority))')
        self.queue.append(item)
        self.fixup_queue(0, len(self.queue)-1)

    """
    Borrowed from the python heap implementation here https://hg.python.org/cpython/file/3.3/Lib/heapq.py
    'heap' is a heap at all indices >= startpos, except possibly for pos.  pos
    is the index of a leaf with a possibly out-of-order value.  Restore the
    heap invariant.
    """
    def fixup_queue(self, startpos, pos):
        newitem = self.queue[pos]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            # parentpos = (pos - 1) >> 1
            parentpos = (pos - 1) // 2
            parent = self.queue[parentpos]
            print("comparing newitem " + str(newitem[1]) + " to olditem " + str(parent[1]))
            if newitem[1] < parent[1]:
                print("newitem " + str(newitem[1]) + " is less than olditem " + str(parent[1]))
                self.queue[pos] = parent
                pos = parentpos
                continue
            print("newitem " + str(newitem[1]) + " is greater than olditem " + str(parent[1]) + " so will insert it here at " + str(pos))
            break
        print("gonna insert " + str(newitem[1]) + " at position " + str(pos))

        self.queue[pos] = newitem
        # print("queue is now: ")
        # self.print_queue()

    def print_queue(self):
        for item in self.queue:
            print(item)

    def peek(self):
        if len(self.queue) < 1:
            raise IndexError('Cannot peek() because there is nothing in the queue')
        return self.queue[0]

p = PriorityQueue()


p.push(('three', 3))
p.push(('four', 4))
p.push(('zero', 0))

p.print_queue()
# print(p.peek())