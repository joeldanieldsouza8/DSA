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

    def __swap(self, current_index, parent_index):
        self.heap[current_index], self.heap[parent_index] = self.heap[parent_index], self.heap[current_index]

    def __heapify_up(self):
        current_index = len(self.heap) - 1

        # Continue to loop until the root node is reached
        while current_index > 0:
            parent_index = self.__parent(current_index)

            # If the parent is larger than the child, swap the values
            if self.heap[parent_index] > self.heap[current_index]:
                self.__swap(current_index, parent_index)

            # Stop if the max-heap property is satisfied
            else:
                break

            current_index = parent_index

    def insert(self, value: int):
        # insert the newNode at the end (last node from left to right.)
        self.heap.append(value)

        # heapify
        self.__heapify_up()


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
