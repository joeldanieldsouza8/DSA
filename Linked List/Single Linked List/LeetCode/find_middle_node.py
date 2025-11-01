from typing import Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self):
        # Initialize an empty list
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def append(self, value: int):
        new_node = Node(value)

        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        return True

    def find_middle_node(self):
        # Check if list is empty
        if self.head is None or self.head.next is None:
            return self.head # Returns None by default if self.head points to nothing
        
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer and fast_pointer.next:
            # We can assert that slow_pointer is not None because the fast_pointer
            # would have terminated the loop long before slow_pointer becomes None.
            # This assertion clarifies the logic for the static type checker.
            assert slow_pointer is not None

            slow_pointer = slow_pointer.next 
            fast_pointer = fast_pointer.next.next

        return slow_pointer


my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

middle_node = my_linked_list.find_middle_node()
if middle_node is not None:
    print(middle_node.value)

"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""
