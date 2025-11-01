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
        self.length = 1

    def append(self, value: int):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            assert self.tail is not None

            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

        return True

    def has_loop(self):
        # Check if there are any nodes in the list
        if self.length < 2:
            return False
        
        # Initialise the pointers
        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer and fast_pointer.next:
            assert slow_pointer is not None

            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            # If the two pointers meet, a loop is detected
            if slow_pointer == fast_pointer:
                return True
            
        # If the loop finishes, it means the 'fast_pointer' reached the end, so no cycle loop exists
        return False


my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop())  # Returns True


my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop())  # Returns False


"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    
"""
