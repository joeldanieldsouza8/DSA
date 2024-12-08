class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

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

    def swap_first_last(self):
        # Check if there are less than 2 nodes which means there is no need to swap them
        if self.length < 2:
            return

        # Check if there are exactly 2 nodes in the list
        if self.length == 2:
            # Swap the current 'head' and 'tail' pointers
            self.head, self.tail = self.tail, self.head

            # Update the pointers for the swapped 'head' and 'tail' pointers
            self.head.next = self.tail
            self.tail.prev = self.head
            self.tail.next = None
            self.head.prev = None

            return

        # Store references to the current 'head' and 'tail' nodes
        head = self.head
        tail = self.tail

        # Store references to the adjacent nodes of the current 'head' and 'tail' nodes
        head_next: Node | None = head.next
        tail_prev: Node | None = tail.prev

        # Update the pointers for the current 'head' and 'tail' nodes
        head.next = None
        head.prev = tail_prev
        tail.prev = None
        tail.next = head_next

        # Update the pointers for the adjacent nodes of the now swapped 'head' and 'tail' nodes
        head_next.prev = tail
        tail_prev.next = head

        # Update the 'head' and 'tail' references in the list
        self.head = tail
        self.tail = head


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)

print('DLL before swap_first_last():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.swap_first_last()

print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    DLL before swap_first_last():
    1
    2
    3
    4

    DLL after swap_first_last():
    4
    2
    3
    1

"""
