class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node({self.value})"


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        """Returns a one-line string representation of the BST in a structured format."""
        if not self.root:
            return "BinarySearchTree: Empty"

        def traverse(node):
            if not node:
                return "None"
            left = traverse(node.left)
            right = traverse(node.right)
            return f"(Value: {node.value}, Left: {left}, Right: {right}])"

        return f"BinarySearchTree: {traverse(self.root)}"

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

    # def min_value(self, starting_node: Node) -> int | None:
    #     # Check if the 'starting_node' is None
    #     if starting_node is None:
    #         raise ValueError("Starting node cannot be None")
    #
    #     return self.__min_value(starting_node)
    #
    # def __min_value(self, current_node: Node) -> int:
    #     # Check if the leaf node is reached
    #     if current_node.left is None:
    #         return current_node.value
    #
    #     # Traverse the left side of the tree as it will always have the min value
    #     return self.__min_value(current_node.left)

    def min_value(self, current_node: Node) -> int:
        while current_node.left is not None:
            current_node = current_node.left

        return current_node.value


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

test1 = my_tree.min_value(my_tree.root)
print(test1)

print(my_tree.min_value(my_tree.root.right))

"""
    EXPECTED OUTPUT:
    ----------------
	18
	52

"""
