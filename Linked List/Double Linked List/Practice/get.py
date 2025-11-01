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
        return " -> ".join(values)

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
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    # This implementation is not the most efficient in terms of time complexity. If the index is closer to the start we can traverse from the 'head'. If the index is closer to the end we can traverse from the 'tail'
    # def get(self, index: int):
    #     # Check if the index is out of bounds
    #     if index < 0 or index > self.length - 1:
    #         return None
    #
    #     # Check if the index is at the start of the list
    #     if index == 0:
    #         return self.head
    #
    #     # Check if the index is at the end of the list
    #     if index == self.length - 1:
    #         return self.tail
    #
    #     else:
    #         curr_node = self.head
    #
    #         for _ in range(index):
    #             curr_node = curr_node.next
    #
    #         return curr_node

    # Time Complexity: O(n/2) ≈ O(n), the time complexity is much better because we have the search space based on close the index is to the start or end of the list
    # Space Complexity: O(1), only using pointers
    def get(self, index: int):
        # Check if the index is out of bounds
        if index < 0 or index >= self.length:
            return None

        # Check if the index is closer to the start of the list
        if index < self.length // 2:  # Using integer floor division
            curr_node = self.head  # Start from the 'head'
            for _ in range(index):
                curr_node = curr_node.next

        else:
            curr_node = self.tail
            for _ in range(self.length - 1, index, -1): # range(start, stop, step)
                curr_node = curr_node.prev

        return curr_node


my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)

print('Get node from first half of DLL:')
print(my_doubly_linked_list.get(1).value)

print('\nGet node from second half of DLL:')
print(my_doubly_linked_list.get(2).value)

"""
    EXPECTED OUTPUT:
    ----------------
    Get node from first half of DLL:
    1

    Get node from second half of DLL:
    2

"""
