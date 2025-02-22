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

    def selection_sort(self):
        # Check if the linked list is empty or contains only one node
        if self.head is None or self.length == 1:
            return self

        n = self.length
        curr_node = self.head # Represents the node to be swapped in the current pass through the list

        for i in range(n - 1):
            min_node = curr_node  # Assume curr_node is the smallest
            temp_node = curr_node.next

            # Traverse the unsorted section of the list
            while temp_node:
                # Update min_node if a smaller element is found
                if temp_node.value < min_node.value:
                    min_node = temp_node

                temp_node = temp_node.next

            # Swap only if a smaller element was found
            if min_node != curr_node:
                curr_node.value, min_node.value = min_node.value, curr_node.value

            curr_node = curr_node.next


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.selection_sort()

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
