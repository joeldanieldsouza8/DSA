class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None

# Recursively build the pre-order binary tree
def build_tree(values: list[int], index: int):
    # Check if we are at the end of the list
    if index >= len(values):
        return None, index

    # Get the value of the current index position in the list
    value = values[index]

    # Update the index position pointer
    index += 1

    # Check if the current value is not valid (because the leaf node doesn't have any children)
    if value == -1:
        return None, index

    # Create a new node
    node = Node(value)

    # Build the left subtree first
    node.left, index = build_tree(values, index)

    # Build the right subtree next
    node.right, index = build_tree(values, index)

    # Return the current node and the updated index
    return node, index

# Recursively print the pre-order binary tree
def print_tree(node: Node | None):
    # Check if the current node is not valid (because the leaf node doesn't have any children)
    if node is None:
        return
    
    # Print the current node
    print(node.value, end=" ")

    # Print all nodes in the left subtree
    print_tree(node.left)

    # Print all nodes in the right subtree
    print_tree(node.right)

def main():
    values = [1, 2, -1, -1, 3, 4, -1, -1, 5, -1, -1]

    # Buid the pre-order binary tree, starting from index 0 (because this becomes the root node)
    root, index = build_tree(values, 0)

    # Print the pre-order binary tree
    print_tree(root)


main()