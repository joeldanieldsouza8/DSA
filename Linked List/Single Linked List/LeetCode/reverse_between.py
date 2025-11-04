from functools import wraps
from typing import Any, Callable, List, Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Node({self.value})"
        
class LinkedList:
    def __init__(self, value: int):
        new_node = Node(value)

        self.head: Optional[Node] = new_node
        self.length = 1

    def __repr__(self) -> str:
        nodes: List[str] = []
        current = self.head

        while current:
            nodes.append(f"Node({current.value})")
            current = current.next

        return f"LinkedList({nodes})"

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        result = " -> ".join(values) if values else "Empty"
        print(result + " -> None")
        return result    
            
    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index: int, end_index: int):
        # Check if the list is empty, has one nodee, or the indices are invalid/the same
        if self.length <= 1 or start_index >= end_index:
            return
        
        # The 'dummy' node keeps track of the 'head' pointer in the list
        dummy = Node(0)
        dummy.next = self.head

        left_prev = dummy

        for _ in range(start_index):
            left_prev = left_prev.next
        
        curr = left_prev.next

        total_number_of_nodes_to_reverse = end_index - start_index + 1

        prev = None

        for _ in range(total_number_of_nodes_to_reverse):
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next

        # Update pointers
        left_prev.next.next = curr
        left_prev.next = prev

        # Re-assign the 'head' pointer to point at the correct node
        self.head = dummy.next


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty()
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1 -> 2 -> 3 -> 4 -> 5 -> None
    Reversed sublist (2, 4): 
    1 -> 2 -> 5 -> 4 -> 3 -> None
    Reversed entire linked list: 
    3 -> 4 -> 5 -> 2 -> 1 -> None
    Reversed sublist of length 1 (3, 3): 
    3 -> 4 -> 5 -> 2 -> 1 -> None
    Reversed empty linked list: 
    Empty -> None
    
"""
