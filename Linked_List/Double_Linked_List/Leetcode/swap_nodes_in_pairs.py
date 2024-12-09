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
        self.length = 1

    def __str__(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        return " <-> ".join(values)

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def swap_pairs(self):
        # Check if there are no nodes in the list
        if self.head is None:
            return

        # Check if there is only one node in the list
        if self.length == 1:
            return

        current = self.head

        # Update the 'head' pointer to the second node in the list as after we swap the first two nodes in the list, the second node will become the first node in the list
        self.head = current.next

        while current and current.next:
            first = current
            second = current.next
            third = current.next.next  # Can be None if this is the last pair

            # Swap first and second. As a good cue, try to always re-arrange the middle pointer node first which in this case is the 'second'
            second.next = first
            second.prev = first.prev
            first.prev = second
            first.next = third

            # Update the previous node's 'next' pointer if it doesn't point to None
            prev_node = second.prev
            if prev_node:
                prev_node.next = second

            # Update third node's 'prev' pointer if it doesn't point to None
            if third:
                third.prev = first

            # Move to the next pair
            current = third



my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs()

print('my_dll after swap_pairs:')
my_dll.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""