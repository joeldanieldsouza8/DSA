from collections import deque


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node({self.value})"


class Queue:
    def __init__(self):
        self.queue = deque()

    def __str__(self):
        return f"Queue: {[str(node) for node in self.queue]}"

    def enqueue(self, node: Node):
        self.queue.append(node)

    def dequeue(self) -> Node:
        return self.queue.popleft()


class Tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return f"Tree(root={self.root})"

    def __insert_recursive(self, curr_node: Node, value: int) -> Node:
        # Check if the leaf node is reached
        if curr_node is None:
            return Node(value)

        # Traverse the left side
        if value < curr_node.value:
            curr_node.left = self.__insert_recursive(curr_node.left, value)

        # Traverse the right side
        if value > curr_node.value:
            curr_node.right = self.__insert_recursive(curr_node.right, value)

        return curr_node

    def insert(self, value: int):  # Check if there are any nodes in the tree
        if self.root is None:
            self.root = Node(value)
            return

        self.__insert_recursive(self.root, value)

    def breadth_first_search(self):
        # Check if there is at least one node in the tree
        if self.root is None:
            return Queue()  # Return an empty queue

        # Initialize a watched and processed queue
        watched = Queue()
        processed = Queue()

        # Initialize the watched queue with the root node
        watched.enqueue(self.root)

        # Continue as long as watched is not empty
        while watched.queue:
            curr_node = watched.dequeue()
            processed.enqueue(curr_node)

            if curr_node.left is not None:
                watched.enqueue(curr_node.left)

            if curr_node.right is not None:
                watched.enqueue(curr_node.right)

        return processed


# Test Case 1
tree = Tree()
for val in [5, 3, 7]:
    tree.insert(val)
bfs_result = tree.breadth_first_search()
print([node.value for node in bfs_result.queue])  # Should print [5, 3, 7]

# Test Case 2
tree = Tree()
for val in [10, 5, 15, 2, 7, 12, 20]:
    tree.insert(val)
bfs_result = tree.breadth_first_search()
print([node.value for node in bfs_result.queue])  # Should print [10, 5, 15, 2, 7, 12, 20]
