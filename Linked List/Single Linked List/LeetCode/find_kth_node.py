from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self, value: int):
        new_node = Node(value)
        self.head: Optional[Node] = new_node
        self.tail: Optional[Node] = new_node

        
    def append(self, value: int):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            assert self.tail is not None

            self.tail.next = new_node
            self.tail = new_node

        return True
  


def find_kth_from_end(linked_list : LinkedList, k: int):       
    # Check if the list is empty or the value of 'k' is out of bounds
    if linked_list.head is None or k <= 0:
        return None
    
    slow_pointer = linked_list.head
    fast_pointer = linked_list.head

    # Move the 'fast_pointer' 'k' steps ahead
    for _ in range(k):
        assert fast_pointer is not None

        fast_pointer = fast_pointer.next

    # Both pointers are now at the correct distances from each other. 
    # Iterate until the 'fast_pointer' now points at 'None'
    while fast_pointer:
        assert slow_pointer is not None

        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next

    return slow_pointer



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value if result is not None else None)  # Output: 4

"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

