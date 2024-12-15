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

    def __str__(self):
        if not self.root:
            return "BinarySearchTree(empty)"

        def traverse(node):
            if not node:
                return "None"
            return f"{node.value} -> (Left: {traverse(node.left)}, Right: {traverse(node.right)})"

        return f"BinarySearchTree(Root: {traverse(self.root)})"

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

    def contains(self, value: int):
        # Check if there are any nodes in the tree
        if self.root is None:
            return False

        current: Node | None = self.root

        while current:
            if value == current.value:
                return True

            # Traverse the right tree
            if value > current.value:
                if current.right is None:
                    return False

                current = current.right

            # Traverse the left tree
            if value < current.value:
                if current.left is None:
                    return False

                current = current.left


##########################################################
##   Test code below will print output to "User logs"   ##
##########################################################


def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")


print("\n----- Test: Contains on Empty Tree -----\n")
bst = BinarySearchTree()
result = bst.contains(5)
check(False, result, "Check if 5 exists in an empty tree:")

print("\n----- Test: Contains Existing Value -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
result = bst.contains(10)
check(True, result, "Check if 10 exists:")
result = bst.contains(5)
check(True, result, "Check if 5 exists:")
result = bst.contains(15)
check(True, result, "Check if 15 exists:")

print("\n----- Test: Contains Not Existing Value -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
result = bst.contains(15)
check(False, result, "Check if 15 exists:")

print("\n----- Test: Contains with Duplicate Inserts -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(10)
result = bst.contains(10)
check(True, result, "Check if 10 exists with duplicate inserts:")

print("\n----- Test: Contains with Left and Right -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(1)
bst.insert(8)
bst.insert(12)
bst.insert(20)
result = bst.contains(1)
check(True, result, "Check if 1 exists:")
result = bst.contains(8)
check(True, result, "Check if 8 exists:")
result = bst.contains(12)
check(True, result, "Check if 12 exists:")
result = bst.contains(20)
check(True, result, "Check if 20 exists:")

