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

    def pop(self):
        # Check if there are any nodes in the list
        if self.head is None:
            return None

        # Check if there is only one node currently in the list
        if self.length == 1:
            remove_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1

            return remove_node

        else:
            remove_node: Node | None = self.tail # The node to be removed
            prev_node: Node | None = remove_node.prev # The node behind the last node
            remove_node.prev = None
            prev_node.next = None
            self.tail = prev_node # Set the 'tail' pointer to point to the node behind the last node
            self.length -= 1

            return remove_node


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_doubly_linked_list.pop().value)
# (0) Items - Returns None
print(my_doubly_linked_list.pop())

"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
