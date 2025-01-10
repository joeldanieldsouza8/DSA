class MinHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return f"{self.heap}"

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def __heapify_down(self):
        # Start from the root node
        current_index = 0
        smallest_index = current_index
        heap_size = len(self.heap)

        while True:
            # Get the index positions of the left and right children
            left_child_index = self._left_child(smallest_index)
            right_child_index = self._right_child(smallest_index)

            # Check if left child exists and is smaller than current smallest
            if (left_child_index < heap_size) and (self.heap[left_child_index] < self.heap[smallest_index]):
                smallest_index = left_child_index

            # Check if right child exists and is smaller than current smallest
            if (right_child_index < heap_size) and (self.heap[right_child_index] < self.heap[smallest_index]):
                smallest_index = right_child_index

            # If current node is already the smallest among itself and its children, we've restored the heap property and can stop
            if smallest_index == current_index:
                break

            # If we found a smaller child, swap current node with the smallest child
            self._swap(current_index, smallest_index)

            # Move down to the swapped position and continue heapifying
            current_index = smallest_index

    def remove(self):
        # Check if the heap is empty
        if not self.heap:
            return None

        root_node = self.heap[0]

        root_index = 0
        last_index = len(self.heap) - 1

        self._swap(root_index, last_index)

        self.heap.pop()

        # Only perform min-heap if there are any nodes remaining in the heap
        if self.heap:
            self.__heapify_down()

        return root_node


myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)
myheap.insert(4)
myheap.insert(2)

print(myheap.heap)  # [2, 6, 4, 12, 8, 10]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 2, Heap: [4, 6, 10, 12, 8]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 4, Heap: [6, 8, 10, 12]

removed = myheap.remove()
print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 6, Heap: [8, 12, 10]

"""
    EXPECTED OUTPUT:
    ----------------
    [2, 6, 4, 12, 8, 10]
    Removed: 2, Heap: [4, 6, 10, 12, 8]
    Removed: 4, Heap: [6, 8, 10, 12]
    Removed: 6, Heap: [8, 12, 10]

"""
