class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def __heapify_up(self):
        current_index = len(self.heap) - 1

        # Continue to loop until the root node is reached
        while current_index > 0:
            parent_index = self._parent(current_index)

            # If the parent is larger than the child, swap the values
            if self.heap[parent_index] < self.heap[current_index]:
                self._swap(current_index, parent_index)

            # Stop if the max-heap property is satisfied
            else:
                break

            current_index = parent_index

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
            if (left_child_index < heap_size) and (self.heap[left_child_index] > self.heap[smallest_index]):
                smallest_index = left_child_index

            # Check if right child exists and is smaller than current smallest
            if (right_child_index < heap_size) and (self.heap[right_child_index] > self.heap[smallest_index]):
                smallest_index = right_child_index

            # If current node is already the smallest among itself and its children, we've restored the heap property and can stop
            if smallest_index == current_index:
                break

            # If we found a smaller child, swap current node with the smallest child
            self._swap(current_index, smallest_index)

            # Move down to the swapped position and continue heapifying
            current_index = smallest_index

    def insert(self, value: int):
        # insert the newNode at the end (last node from left to right.)
        self.heap.append(value)

        # heapify
        self.__heapify_up()

    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.__heapify_down()

        return max_value

def find_kth_smallest(nums: list[int], k: int) -> int | bool:
    # Check if 'k' is within bounds
    if k <= 0 or k > len(nums):
        return False

    max_heap = MaxHeap()

    for num in nums:
        # Add each number to the heap, where the 'insert' method will apply the max-heap property
        max_heap.insert(num)

        # Check if the size of the heap exceeds 'k'
        if len(max_heap.heap) > k:
            # Remove the current largest number in the heap which will result in the 'k' smallest number in the heap overall
            max_heap.remove()

    # Return the root of the max-heap which is the kth smallest element in 'nums'
    return max_heap.heap[0]

# Test cases
nums = [[3, 2, 1, 5, 6, 4], [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6], [3, 2, 3, 1, 2, 4, 5, 5, 6]]
ks = [2, 3, 4, 7]
expected_outputs = [2, 3, 4, 5]

for i in range(len(nums)):
    print(f'Test case {i + 1}...')
    print(f'Input: {nums[i]} with k = {ks[i]}')
    result = find_kth_smallest(nums[i], ks[i])
    print(f'Output: {result}')
    print(f'Expected output: {expected_outputs[i]}')
    print(f'Test passed: {result == expected_outputs[i]}')
    print('---------------------------------------')

"""
    EXPECTED OUTPUT:
    ----------------
    Test case 1...
    Input: [3, 2, 1, 5, 6, 4] with k = 2
    Output: 2
    Expected output: 2
    Test passed: True
    ---------------------------------------
    Test case 2...
    Input: [6, 5, 4, 3, 2, 1] with k = 3
    Output: 3
    Expected output: 3
    Test passed: True
    ---------------------------------------
    Test case 3...
    Input: [1, 2, 3, 4, 5, 6] with k = 4
    Output: 4
    Expected output: 4
    Test passed: True
    ---------------------------------------
    Test case 4...
    Input: [3, 2, 3, 1, 2, 4, 5, 5, 6] with k = 7
    Output: 5
    Expected output: 5
    Test passed: True
    ---------------------------------------

"""
