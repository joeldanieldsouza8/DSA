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

    # def __str__(self):
    #     return f"{self.}"

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

    def r_contains(self, value: int) -> bool:
        return self.__r_contains(self.root, value)

    def __r_contains(self, current_node: Node, value: int) -> bool:
        # Check if the current node is pointing to null, which means that the node containing the desired value is not found
        if current_node is None:
            return False

        # Check if the current node's value is equal to the desired value
        if current_node.value == value:
            return True

        # Otherwise, continue to traverse through the tree
        # Check if the right subtree should be traversed
        if value > current_node.value:
            current_node = current_node.right
            return self.__r_contains(current_node, value)

        # Check if the left subtree should be traversed
        if value < current_node.value:
            current_node = current_node.left
            return self.__r_contains(current_node, value)


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.r_contains(27))

print('\nBST Contains 17:')
print(my_tree.r_contains(17))

"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""

