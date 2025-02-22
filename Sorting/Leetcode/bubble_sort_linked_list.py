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

    def bubble_sort(self):
        # Check if the linked list is empty or contains only one node
        if self.head is None or self.length == 1:
            return self

        stop: Node | None = None  # Keeps track of the last sorted position

        while True:
            swapped = False
            curr_node: Node | None = self.head  # Reset the current pointer back to the head
            next_node: Node | None = curr_node.next

            while next_node and (next_node != stop):
                # Swap the values of the nodes
                if curr_node.value > next_node.value:
                    curr_node.value, next_node.value = next_node.value, curr_node.value
                    swapped = True

                curr_node = curr_node.next
                next_node = next_node.next

            stop = curr_node  # The 'stop' node is now at the position where the 'curr_node' terminated

            # If no swaps happened through the current pass through the list, then it means that all the nodes are in the correct position and the list is now sorted
            if not swapped:
                break


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

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
