class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node({self.value})"


class Tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return f"Tree(root={self.root})"

    def insert(self, value: int):  # Check if there are any nodes in the tree
        if self.root is None:
            self.root = Node(value)
            return

        def insert_recursive(curr_node: Node, value: int) -> Node:
            # Check if the leaf node is reached
            if curr_node is None:
                return Node(value)

            # Traverse the left side
            if value < curr_node.value:
                curr_node.left = insert_recursive(curr_node.left, value)

            # Traverse the right side
            elif value > curr_node.value:  # Prevents duplicates
                curr_node.right = insert_recursive(curr_node.right, value)

            return curr_node

        insert_recursive(self.root, value)

    def dfs_pre_order(self) -> list[Node]:
        # Initialize a list to keep track of the visited nodes
        results = []

        def traverse(cur_node: Node):
            results.append(cur_node.value)  # Add the current node's value

            # Traverse to the left side of the current node
            if cur_node.left is not None:
                traverse(cur_node.left)

            # Traverse to the right side of the current node
            if cur_node.right is not None:
                traverse(cur_node.right)

        traverse(self.root)

        return results

    # left-right-parent
    def dfs_post_order(self) -> list[Node]:
        # Initialize a list to keep track of the visited nodes
        results = []

        def traverse(cur_node: Node):
            # Traverse to the left side of the current node
            if cur_node.left is not None:
                traverse(cur_node.left)

            # Traverse to the right side of the current node
            if cur_node.right is not None:
                traverse(cur_node.right)

            results.append(cur_node.value)  # Add the current node's value

        traverse(self.root)

        return results

    # left-parent-right
    def dfs_in_order(self) -> list[Node]:
        # Initialize a list to keep track of the visited nodes
        results = []

        def traverse(cur_node: Node):
            # Traverse to the left side of the current node
            if cur_node.left is not None:
                traverse(cur_node.left)

            results.append(cur_node.value)  # Add the current node's value

            # Traverse to the right side of the current node
            if cur_node.right is not None:
                traverse(cur_node.right)

        traverse(self.root)

        return results


def test_dfs_pre_order():
    # Test Case 1: Basic tree structure
    tree1 = Tree()
    tree1.insert(10)
    tree1.insert(5)
    tree1.insert(15)
    tree1.insert(3)
    tree1.insert(7)

    assert tree1.dfs_pre_order() == [10, 5, 3, 7, 15], "Test Case 1 Failed"

    # Test Case 2: Tree with only a single node (edge case)
    tree2 = Tree()
    tree2.insert(42)

    assert tree2.dfs_pre_order() == [42], "Test Case 2 Failed"

    print("All test cases for dfs_pre_order passed!")


test_dfs_pre_order()
