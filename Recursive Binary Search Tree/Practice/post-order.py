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

    # Left-Root-Right
    # In the first "processing" cycle, from the root node, go all the way down to the leaf node in the left subtree
    # Process that leaf node
    # Check if the leaf node has a sibling (right node)
    # If yes, go back up to its parent node and then down to the sibling (right node) and process this sibling (right node)
    # Then go back to the parent node, and process this
    def __post_order_recursive(self, node: Node, result: list[Node]):
        # Continue only if the node is not null
        if node is None:
            return

        self.__post_order_recursive(node.left, result)
        self.__post_order_recursive(node.right, result)
        result.append(node)

        return result

    def post_order(self) -> list[Node]:
        result: list[Node] = []

        # Start at the root node
        result = self.__post_order_recursive(self.root, result)

        return result

    def r_insert(self, value: int) -> Node:
        # Check if there are no nodes in the tree
        if self.root is None:
            self.root = Node(value)
            return self.root

        return self.__r_insert(self.root, value)

    def __r_insert(self, current_node: Node, value: int) -> Node:
        if current_node is None:
            return Node(value)

        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)

        # If value == current_node.value, do nothing (no duplicates allowed)
        return current_node

def test_post_order_traversal():
    bst = BinarySearchTree()

    values = [8, 4, 12, 2, 6]

    for value in values:
        bst.r_insert(value)

    print("Post-order traversal:")
    nodes = bst.post_order()
    for node in nodes:
        print(node, end=" ")  # Will print: Node(2) Node(6) Node(4) Node(12) Node(8)

def main():
    test_post_order_traversal()

if __name__ == "__main__":
    main()