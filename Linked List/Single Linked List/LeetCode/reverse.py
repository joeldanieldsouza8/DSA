from typing import Optional

class Node:
    def __init__(self, val: int, next: 'Node | None'):
        self.val = val
        self.next = next

def reverseList(head: Optional[Node]) -> Optional[Node]:
    # Check if the list is empty
    if head is None:
        return None

    previous = None
    current = head

    while current is not None:
        # Save the position of the next node
        following = current.next

        # Reverse the 'next' pointer of the 'current' node
        current.next = previous

        # Update the pointer variables to move one step ahead
        previous = current
        current = following

    # Update the 'head' pointer 
    head = previous

    return head