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

    def has_loop(self):
        # Check if there are any nodes in the list
        if self.head is None:
            return False

        # Space complexity: O(1) - As we are using pointers and no additional storage data structure
        fast_pointer = self.head
        slow_pointer = self.head

        # count = 0

        # Time Complexity: O(n) - As we need to traverse through the list once or many times until the two pointers ('fast_pointer' and 'slow_pointer') meet 
        # Continue to iterate through the list as long as the 'next' pointer of the last node isn't null
        # The objective of using the 'fast_pointer' and 'slow_pointer' is that at some point the two pointers will meet indicating there is a loop in the list
        while fast_pointer is not None and fast_pointer.next is not None:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            # count += 1

            if fast_pointer == slow_pointer:
                # print(f"Total iterations: {count}")
                return True

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
