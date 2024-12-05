class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"Node({self.value})"


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def __str__(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        return " -> ".join(values)

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
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.length = 0

    def reverse_between(self, start_index: int, end_index: int):
        # Check if the index values are not out of bounds
        if (start_index < 0 or end_index < 0) or (start_index > self.length or end_index > self.length) or (self.head is None) or (start_index == end_index):
            return

        # Using the 'dummy_node' to handle edge case where we might want to swap the first and last node in the list
        dummy_node = Node(0)
        dummy_node.next = self.head

        prev_start_ptr: Node | None = dummy_node # The 'prev' pointer is always one behind the 'curr' pointer
        # curr_start_ptr = self.head

        # This will loop until the node before the first node to be swapped
        for _ in range(start_index):
            prev_start_ptr = prev_start_ptr.next

        curr_start_ptr: Node | None = prev_start_ptr.next # Points to the first node to be swapped

        # Calculate the number of nodes to reverse
        num_nodes_to_reverse = end_index - start_index

        # This will loop until the node before the second node to be swapped
        for _ in range(num_nodes_to_reverse):
            # Detach the node after curr_start_ptr
            temp: Node | None = curr_start_ptr.next
            curr_start_ptr.next = temp.next

            # Move the detached node to the front of the section
            temp.next = prev_start_ptr.next
            prev_start_ptr.next = temp

        self.head = dummy_node.next

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
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None

"""
