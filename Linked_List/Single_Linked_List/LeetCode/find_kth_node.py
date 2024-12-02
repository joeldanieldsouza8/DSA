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


def find_kth_from_end(linked_list: LinkedList, k_value: int):
    # Check if the list is empty or 'k_value' is not out of bounds
    if linked_list.head is None or k_value <= 0:
        return None

    # Space Complexity: O(1)
    first_ptr = linked_list.head
    second_ptr = linked_list.head

    # Time Complexity: O(n) - As we are traversing through all the nodes in the list
    # Move the 'first_ptr' 'k' steps ahead, based on the distance, from the 'second_ptr'
    for _ in range(k_value):
        # Check if the 'k_value' is not out of bounds
        if first_ptr is None:
            return None

        first_ptr = first_ptr.next

    # Now both pointers are at their correct starting position. Move both pointers one step at a time until `first_ptr` points to the last node in the list
    while first_ptr:
        first_ptr = first_ptr.next
        second_ptr = second_ptr.next

    return second_ptr


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4

"""
    EXPECTED OUTPUT:
    ----------------
    4

"""
