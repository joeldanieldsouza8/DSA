﻿class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        # Check if there are any nodes in the queue
        if self.length == 0:
            return

        removed_node = self.first

        # Check if there is one node in the queue
        if self.length == 1:
            self.first = None
            self.last = None

        else:
            self.first = self.first.next
            removed_node.next = None

        self.length -= 1
        return removed_node


my_queue = Queue(1)
my_queue.enqueue(2)

# (2) Items - Returns 2 Node
print(my_queue.dequeue().value)
# (1) Item -  Returns 1 Node
print(my_queue.dequeue().value)
# (0) Items - Returns None
print(my_queue.dequeue())

"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    None

"""