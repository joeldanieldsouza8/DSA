class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node({self.value})"


class BinarySearchTree:
    def __init__(self):
        self.root: Node | None = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False

            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left

            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def kth_smallest(self, k_value: int):
        count = 0
        visited = []
        curr = self.root  # Begin the traversal at the root node

        while True:
            # Traverse the left side of the tree
            while curr is not None:
                visited.append(curr)  # Add each node to the visited stack
                curr = curr.left  # Move to the left child

            # Return to the parent node
            curr = visited.pop()  # Process the node
            count += 1  # Increment the count to signify that a node has been processed in-order

            # Check if the count equals the k_value to find the kth node in-order
            if count == k_value:
                return curr.value

            # Otherwise, move to the right subtree of the current node
            curr = curr.right


bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.kth_smallest(1))  # Expected output: 2
print(bst.kth_smallest(3))  # Expected output: 4
print(bst.kth_smallest(6))  # Expected output: 7

"""
    EXPECTED OUTPUT:
    ----------------
    2
    4
    7
    
 """
