class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    # Remove the first node from the list
    def pop_first(self):
        # Check if there are any nodes currently in the list
        if self.head is None:
            return None

        # Check if there is currently only one node in the list
        if self.length == 1:
            curr_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1

            return curr_node

        else:
            curr_node = self.head
            self.head = self.head.next
            curr_node.next = None
            self.length -= 1

            return curr_node


my_linked_list = LinkedList(2)
my_linked_list.append(1)

# (2) Items - Returns 2 Node
print(my_linked_list.pop_first().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop_first().value)
# (0) Items - Returns None
print(my_linked_list.pop_first())

"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
