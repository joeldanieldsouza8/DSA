from typing import TypeAlias

from collections import deque

NodeLabel: TypeAlias = str
AdjacencyList: TypeAlias = dict[NodeLabel, list[NodeLabel]]

def breadth_first_search(graph: AdjacencyList, start_node: NodeLabel) -> list[NodeLabel] | None:
    # Check if the start node doesn't exist in the graph
    if start_node not in graph:
        return None
    
    visited_nodes: set[NodeLabel] = set()
    exploration_queue: deque[NodeLabel] = deque() # Note: 'dequeue' is implemented as a linked list behind-the-scenes
    traversal_order: list[NodeLabel] = []

    # Initialise the queue with the starting node
    visited_nodes.add(start_node)
    exploration_queue.append(start_node)

    # Continue as long as there are still nodes to process in the graph
    while exploration_queue:
        current_node = exploration_queue.popleft()
        traversal_order.append(current_node)

        # Explore the adjacent (or neighbour) nodes of the current node
        for neighbouring_node in graph[current_node]:
            # Check if the neighbouring node hasn't been visited yet
            if neighbouring_node not in visited_nodes:
                # Mark the node as visited and add to the queue to be processed
                visited_nodes.add(neighbouring_node)
                exploration_queue.append(neighbouring_node)

    return traversal_order





social_network: AdjacencyList = {
    "Alice": ["Bob", "Carol"],
    "Bob":   ["Alice", "Dave", "Eve"],
    "Carol": ["Alice", "Frank"],
    "Dave":  ["Bob"],
    "Eve":   ["Bob"],
    "Frank": ["Carol"],
}

discovery_order: list[NodeLabel] | None = breadth_first_search(social_network, start_node="Alice")
print(discovery_order) # Output: ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank']