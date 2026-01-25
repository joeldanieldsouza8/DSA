from typing import List, Optional


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Node({self.value})"
        
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

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        result = " -> ".join(values) if values else "Empty"
        print(result + " -> None")
        return result  
            
    def make_empty(self):
        self.head = None
        self.length = 0
 

    def swap_pairs(self):
        # Check if there are no nodes or only one node in the list
        if self.length < 2 or self.head is None:
            return
        
        dummy = Node(-1)
        dummy.next = self.head

        prev_node = dummy
        
        while prev_node.next and prev_node.next.next:
            node_1 = prev_node.next
            node_2 = node_1.next

            node_1.next = node_2.next
            node_2.next = node_1
            prev_node.next = node_2

            prev_node = node_1

        # Reset the 'head' pointer to the correct position
        self.head = dummy.next



# Test case 1: Swapping pairs in a list with an even number of nodes (1->2->3->4)
print("\nTest case 1: Swapping pairs in a list with an even number of nodes.")
ll1 = LinkedList(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
print("BEFORE: ", end="")
ll1.print_list()
print("AFTER:  ", end="")
ll1.swap_pairs()
ll1.print_list()
print("-----------------------------------")

# Test case 2: Swapping pairs in a list with an odd number of nodes (1->2->3->4->5)
print("\nTest case 2: Swapping pairs in a list with an odd number of nodes.")
ll2 = LinkedList(1)
ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(5)
print("BEFORE: ", end="")
ll2.print_list()
print("AFTER:  ", end="")
ll2.swap_pairs()
ll2.print_list()
print("-----------------------------------")

# Test case 3: Swapping pairs in a list with a single node (1)
print("\nTest case 3: Swapping pairs in a list with a single node.")
ll3 = LinkedList(1)
print("BEFORE: ", end="")
ll3.print_list()
print("AFTER:  ", end="")
ll3.swap_pairs()
ll3.print_list()
print("-----------------------------------")

# Test case 4: Swapping pairs in an empty list
print("\nTest case 4: Swapping pairs in an empty list.")
ll4 = LinkedList(1)
ll4.make_empty()
print("BEFORE: ", end="")
ll4.print_list()
print("AFTER:  ", end="")
ll4.swap_pairs()
ll4.print_list()
print("-----------------------------------")

# Test case 5: Swapping pairs in a list with two nodes (1->2)
print("\nTest case 5: Swapping pairs in a list with two nodes.")
ll5 = LinkedList(1)
ll5.append(2)
print("BEFORE: ", end="")
ll5.print_list()
print("AFTER:  ", end="")
ll5.swap_pairs()
ll5.print_list()
print("-----------------------------------")


