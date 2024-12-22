class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index: int):
        return 2 * index + 1

    def _right_child(self, index: int):
        return 2 * index + 2

    def _parent(self, index: int):
        return (index - 1) // 2

    def _swap(self, index1: int, index2: int):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value: int):
        # Add the new value to the end of the heap (list) to maintain the complete binary structure (add value from left-right)
        # print(f"Length BEFORE Insertion: {self.heap[len(self.heap) - 1] if len(self.heap) != 0 else None}")
        self.heap.append(value)
        # print(f"Length AFTER Insertion: {self.heap[len(self.heap) - 1]}")

        # Bubble up the heap tree to restore the max heap property
        current_index = len(
            self.heap) - 1  # Initially, this represents the index position of the new value inserted at the end of the list

        while current_index > 0:
            # Find the parent index
            parent_index = self._parent(current_index)

            # If the current element is greater than its parent element, swap them
            if self.heap[current_index] > self.heap[parent_index]:
                self._swap(current_index, parent_index)
                # Move up to the parent's index
                current_index = parent_index

            else:
                # If the heap property is satisfied, stop
                break


myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)

print(myheap.heap)

myheap.insert(100)

print(myheap.heap)

# myheap.insert(75)
#
# print(myheap.heap)

"""
    EXPECTED OUTPUT:
    ----------------
    [99, 72, 61, 58]
    [100, 99, 61, 58, 72]
    [100, 99, 75, 58, 72, 61]

"""
