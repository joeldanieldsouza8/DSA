from typing import Self


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __repr__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        if not elements:
            return "LinkedList()"
        return f"LinkedList({' -> '.join(elements)})"

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
            self.tail = new_node
        self.length += 1

    def merge(self, linked_list_2: Self):
        # Check for empty lists
        if linked_list_2.head is None:
            return

        if self.head is None:
            self.head = linked_list_2.head
            self.tail = linked_list_2.tail
            self.length = linked_list_2.length
            return

        # Initialize a dummy node
        dummy_node = Node(-1)
        current = dummy_node
        current_1 = self.head
        current_2 = linked_list_2.head

        # Simultaneously iterate through both linked lists
        # Iterate through the lists as long as the end of either list is not reached
        while current_1 and current_2:
            if current_1.value < current_2.value:
                current.next = current_1
                current_1 = current_1.next

            else:
                current.next = current_2
                current_2 = current_2.next

            current = current.next

        # Add remaining nodes
        if current_1:
            current.next = current_1  # Attach the entire remaining chain at once
            new_tail = self.tail

        else:
            current.next = current_2  # Attach the entire remaining chain at once
            new_tail = linked_list_2.tail

        # Update head, tail and length
        self.head = dummy_node.next
        self.tail = new_tail  # The code ensures one of the two branches (if or else) will always run. This means 'new_tail' is always assigned a value before it’s used.
        self.length += linked_list_2.length


linked_list_1 = LinkedList(1)
linked_list_1.append(3)
linked_list_1.append(5)
linked_list_1.append(7)

linked_list_2 = LinkedList(2)
linked_list_2.append(4)
linked_list_2.append(6)
linked_list_2.append(8)

linked_list_1.merge(linked_list_2)

linked_list_1.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""
