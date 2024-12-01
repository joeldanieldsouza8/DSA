﻿class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f"Node({self.value})"


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        return " -> ".join(values)

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
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index: int, value: int):
        # Check if index is not out of bounds
        if index < 0 or index > self.length:
            return None

        # Check if the index is at the start of the list
        if index == 0:
            return self.prepend(value)

        # Check if the index is at the end of the list
        if index == self.length:
            return self.append(value)

        else:
            new_node = Node(value)

            prev_node = self.get(index - 1)  # Get the previous node at the desired index position
            curr_node = prev_node.next  # Get the current node at the desired index position

            # Swap the 'next' and 'prev' pointers
            prev_node.next = new_node
            new_node.prev = prev_node
            new_node.next = curr_node
            curr_node.prev = new_node

            self.length += 1
            return True


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(3)

print('DLL before insert():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.insert(1, 2)

print('\nDLL after insert(2) in middle:')
my_doubly_linked_list.print_list()

my_doubly_linked_list.insert(0, 0)

print('\nDLL after insert(0) at beginning:')
my_doubly_linked_list.print_list()

my_doubly_linked_list.insert(4, 4)

print('\nDLL after insert(4) at end:')
my_doubly_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    DLL before insert():
    1
    3

    DLL after insert(2) in middle:
    1
    2
    3

    DLL after insert(0) at beginning:
    0
    1
    2
    3

    DLL after insert(4) at end:
    0
    1
    2
    3
    4

"""