class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value: int):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        curr_node = self.head  # Set the pointer to point to the head of the linked list

        # Continue iterating through the linked list as long as the current node that the pointer is pointing to is not null
        while curr_node is not None:
            print(curr_node.value) # Print the value of the current node that the pointer is pointing to
            curr_node = curr_node.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value: int):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    1
    2
    3

"""
