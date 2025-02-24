class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Node | None = None

    def __str__(self):
        return f"Node({self.value})"


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        result = []
        temp = self.head
        while temp:
            result.append(str(temp.value))
            temp = temp.next
        return " -> ".join(result) + f" | Length: {self.length}"

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
            self.tail = new_node
        self.length += 1

    def insertion_sort(self):
        # Check if there is 1 or fewer nodes in the list
        if self.length < 2:
            return

        # Create a 'dummy' node to simply insertions at the start of the list
        dummy = Node(0)
        current = self.head

        while current:
            # Reset the 'prev' pointer to point back to the 'dummy' node
            prev = dummy
            next_node = current.next

            # Traverse the sorted sub-list to find the insertion point for the 'current' node
            while prev.next and prev.next.value < current.value:
                prev = prev.next

            # Insert the 'current' node at the correction insertion point/location
            current.next = prev.next
            prev.next = current

            # Move to the next node in the unsorted part of the list
            current = next_node

        # Update the 'head' pointer to the correct position in the list
        self.head = dummy.next

        # Update the 'tail' pointer to the correct position in the list
        temp = self.head
        while temp and temp.next:
            temp = temp.next

        self.tail = temp


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""
