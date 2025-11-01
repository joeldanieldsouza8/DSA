from functools import wraps
from typing import Any, Callable, List, Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Node({self.value})"

def convert_linkedlist_to_list(head: Optional[Node]) -> List[int]:
    """
    Convert a linked list starting from the 'head' to a list.
    """

    result: List[int] = []
    curr_pointer = head

    while curr_pointer:
        result.append(curr_pointer.value)
        curr_pointer = curr_pointer.next

    return result

class LinkedList:
    def __init__(self, value: int):
        new_node = Node(value)

        self.head: Optional[Node] = new_node
        self.length = 1

    def __repr__(self) -> str:
        nodes: List[str] = []
        current = self.head

        while current:
            nodes.append(f"Node({current.value})")
            current = current.next

        return f"LinkedList({nodes})"
        

    def append(self, value: int):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    # My original working implementation
    """
    def partition_list(self, x_value: int):
        # Check if the list is empty
        if self.head is None or self.length == 0:
            return None

        # For nodes with values less than the 'x_value'
        less_head_node = Node(-1)
        less_pointer: Optional[Node] = less_head_node

        # For nodes with values greater than or equal to the 'x_value'
        greater_head_node = Node(-1)
        greater_pointer: Optional[Node] = greater_head_node

        # Pointer to traverse the original list
        curr_pointer: Optional[Node] = self.head

        for _ in range(self.length):
            assert curr_pointer is not None

            if curr_pointer.value < x_value:
                less_pointer.next = curr_pointer
                less_pointer = less_pointer.next
                curr_pointer = curr_pointer.next
                less_pointer.next = None

            else:
                greater_pointer.next = curr_pointer
                greater_pointer = greater_pointer.next
                curr_pointer = curr_pointer.next
                greater_pointer.next = None

        if less_head_node.next is not None:
            self.head = less_head_node.next

        else:
            self.head = greater_head_node.next

        temp = greater_head_node.next

        less_head_node.next = None
        greater_head_node.next = None

        less_pointer.next = temp

        return self
    """

    def partition_list(self, x_value: int):
        # Check if the list is empty
        if self.head is None or self.length == 0:
            return None

        # For nodes with values less than the 'x_value'
        less_head_node = Node(-1)
        less_pointer: Optional[Node] = less_head_node

        # For nodes with values greater than or equal to the 'x_value'
        greater_head_node = Node(-1)
        greater_pointer: Optional[Node] = greater_head_node

        # Pointer to traverse the original list
        curr_pointer: Optional[Node] = self.head

        while curr_pointer:
            assert curr_pointer is not None

            if curr_pointer.value < x_value:
                less_pointer.next = curr_pointer
                less_pointer = curr_pointer

            else:
                greater_pointer.next = curr_pointer
                greater_pointer = curr_pointer

            curr_pointer = curr_pointer.next

        # Connect the 'next' pointer of the last node in the list of the less than 'x_value' to the first node in the list of the greater than or equal to 'x_value'
        greater_pointer.next = None
        less_pointer.next = greater_head_node.next

        # Update the 'head' pointer to point to the first node in the list of the less than 'x_value'
        self.head = less_head_node.next

        # Detach the 'next' pointers of the two dummy nodes
        less_head_node.next = None
        greater_head_node.next = None

#  +=====================================================+
#  |                                                     |
#  |          THE TEST CODE BELOW WILL PRINT             |
#  |              OUTPUT TO "USER LOGS"                  |
#  |                                                     |
#  |  Use the output to test and troubleshoot your code  |
#  |                                                     |
#  +=====================================================+


# Function to test partition_list
def test_partition_list():
    test_cases_passed = 0

    print("-----------------------")

    # Test 1: Normal Case
    print("Test 1: Normal Case")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    ll.append(5)
    print("Before:", convert_linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", convert_linkedlist_to_list(ll.head))
    if convert_linkedlist_to_list(ll.head) == [1, 2, 3, 4, 5]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")

    print("-----------------------")

    
    # Test 2: All Equal Values
    print("Test 2: All Equal Values")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(3)
    ll.append(3)
    print("Before:", convert_linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", convert_linkedlist_to_list(ll.head))
    if convert_linkedlist_to_list(ll.head) == [3, 3, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 3: Single Element
    print("Test 3: Single Element")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(1)
    print("Before:", convert_linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", convert_linkedlist_to_list(ll.head))
    if convert_linkedlist_to_list(ll.head) == [1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 4: Already Sorted
    print("Test 4: Already Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    print("Before:", convert_linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", convert_linkedlist_to_list(ll.head))
    if convert_linkedlist_to_list(ll.head) == [1, 2, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 5: Reverse Sorted
    print("Test 5: Reverse Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(2)
    ll.append(1)
    print("Before:", convert_linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", convert_linkedlist_to_list(ll.head))
    if convert_linkedlist_to_list(ll.head) == [1, 3, 2]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 6: All Smaller Values
    print("Test 6: All Smaller Values")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(1)
    ll.append(1)
    print("Before:", convert_linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", convert_linkedlist_to_list(ll.head))
    if convert_linkedlist_to_list(ll.head) == [1, 1, 1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 7: Single Element, Equal to Partition
    print("Test 7: Single Element, Equal to Partition")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    print("Before:", convert_linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", convert_linkedlist_to_list(ll.head))
    if convert_linkedlist_to_list(ll.head) == [3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Summary
    print(f"{test_cases_passed} out of 7 tests passed.")


# Run the test function
test_partition_list()
