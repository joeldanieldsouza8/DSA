﻿class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        # Check if there are no nodes in the list
        if self.head is None:
            return None

        # Check if there is only one node in the list
        if self.length == 1:
            remove_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1

            return remove_node

        else:
            remove_node = self.head
            self.head = remove_node.next
            self.head.prev = None
            remove_node.next = None
            self.length -= 1

            return remove_node


my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(1)

# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop_first().value)
# (1) Item -  Returns 1 Node
print(my_doubly_linked_list.pop_first().value)
# (0) Items - Returns None
print(my_doubly_linked_list.pop_first())

"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
