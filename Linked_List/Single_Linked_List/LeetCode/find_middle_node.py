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

    def __str__(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        return " -> ".join(values)

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def find_middle_node(self):
        # Check if there are any nodes in the list
        if self.head is None:
            return None


        fast_pointer: Node | None = self.head  # Fast pointer moves two steps at a time
        slow_pointer: Node | None = self.head  # Slow pointer moves one step at a time

        # Iterate the list until you are at the last node in the list (for odd number of total nodes in the list), at which point the 'slow_pointer' will point at the middle node in the list. Or until you are at the first node in the second-half of the list (for even number of total nodes in the list)
        while fast_pointer is not None and fast_pointer.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

        return slow_pointer


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
# my_linked_list.append(5)

print(my_linked_list.find_middle_node().value)

"""
    EXPECTED OUTPUT:
    ----------------
    3

"""
