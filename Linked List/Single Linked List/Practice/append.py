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

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Adds a new node to the end of the linked list
    def append(self, value):
        new_node = Node(value)  # Create a new node to add to the linked list

        # Check if there are current no nodes in the linked list
        if self.head is None:
            # Point the head and tail to the new node as there weren't any nodes previously in the linked list
            self.head = new_node
            self.tail = new_node

        else:
            curr_node = self.tail  # Create a temporary pointer to point to the end (tail node) of the linked list
            curr_node.next = new_node  # Set the previous node (which was the tail node in the linked list) to point to the new node
            self.tail = new_node  # Point the tail to the new node that has just been added to the end of the linked list

        self.length += 1  # Increment the length of the linked list as a new node has been added to the linked list


my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.append(1)
my_linked_list.append(2)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Linked List:
    1
    2

"""
