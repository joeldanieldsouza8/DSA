class Node:
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
        return " <-> ".join(values)

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

    def reverse(self):
        # Check if there are any nodes in the list
        if self.head is None:
            return

        # Store references to the current 'head' and 'tail' nodes
        head = self.head
        tail = self.tail

        prev_node: Node | None = None
        curr_node: Node | None = self.head

        while curr_node:
            # Update the pointer to point to the next node in the list
            next_node: Node | None = curr_node.next

            # Swap the 'next' and 'prev' pointers of the current node - 'curr_node'
            curr_node.next = prev_node
            curr_node.prev = next_node

            # Move to the next node in the list
            prev_node = curr_node
            curr_node = next_node

        self.head = tail
        self.tail = head


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print('DLL before reverse():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.reverse()

print('\nDLL after reverse():')
my_doubly_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    DLL before reverse():
    1
    2
    3
    4
    5

    DLL after reverse():
    5
    4
    3
    2
    1

"""
