class MinHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return f"{self.heap}"

    def __left_child(self, index):
        return 2 * index + 1

    def __right_child(self, index):
        return 2 * index + 2

    def __parent(self, index):
        return (index - 1) // 2

    def __swap(self, current, parent):
        self.heap[current], self.heap[parent] = self.heap[parent], self.heap[current]

    def __heapify(self):
        """Performs Min-Heap"""

        # Points to the INDEX of the last node in the tree
        current = len(self.heap) - 1

        # Continue swapping until the root node is reached
        while current > 0:
            # Find the INDEX of the PARENT node of the CURRENT node
            parent = (current - 1) // 2

            # Check if the value of the CURRENT node is smaller than the value of its PARENT node
            if self.heap[current] < self.heap[parent]:
                self.__swap(current, parent)
                current = parent

            else:
                break

    def insert(self, value: int):
        # insert the newNode at the end (last node from left to right.)
        self.heap.append(value)

        # heapify
        self.__heapify()


myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)

print(myheap.heap)  # [6, 8, 10, 12]

myheap.insert(4)

print(myheap.heap)  # [4, 6, 10, 12, 8]

myheap.insert(2)

print(myheap.heap)  # [2, 6, 4, 12, 8, 10]

"""
    EXPECTED OUTPUT:
    ----------------
    [6, 8, 10, 12]
    [4, 6, 10, 12, 8]
    [2, 6, 4, 12, 8, 10]

"""
