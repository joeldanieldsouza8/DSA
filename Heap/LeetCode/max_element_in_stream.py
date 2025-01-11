class MaxHeap:
    def __init__(self):
        self.heap = []

    def __left_child(self, index):
        return 2 * index + 1

    def __right_child(self, index):
        return 2 * index + 2

    def __parent(self, index):
        return (index - 1) // 2

    def __swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def __heapify_up(self):
        current_index = len(self.heap) - 1

        # Continue to loop until the root node is reached
        while current_index > 0:
            parent_index = self.__parent(current_index)

            # If the parent is larger than the child, swap the values
            if self.heap[parent_index] < self.heap[current_index]:
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

    def __heapify_down(self):
        # Start from the root node
        current_index = 0
        smallest_index = current_index
        heap_size = len(self.heap)

        while True:
            # Get the index positions of the left and right children
            left_child_index = self.__left_child(smallest_index)
            right_child_index = self.__right_child(smallest_index)

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
            self.__swap(current_index, smallest_index)

            # Move down to the swapped position and continue heapifying
            current_index = smallest_index

    def remove(self):
        # Check if the heap is empty
        if not self.heap:
            return None

        root_node = self.heap[0]

        root_index = 0
        last_index = len(self.heap) - 1

        self.__swap(root_index, last_index)

        self.heap.pop()

        # Only perform min-heap if there are any nodes remaining in the heap
        if self.heap:
            self.__heapify_down()

        return root_node


def stream_max(nums: list[int]) -> list[int]:
    max_heap = MaxHeap()
    result = []

    for num in nums:
        # By inserting each number into the heap, it results in the largest number at the root node
        max_heap.insert(num)

        largest_value = max_heap.heap[0]
        result.append(largest_value)

    return result


test_cases = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
    ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1])
]

for i, (nums, expected) in enumerate(test_cases):
    result = stream_max(nums)
    print(f'\nTest {i + 1}')
    print(f'Input: {nums}')
    print(f'Expected Output: {expected}')
    print(f'Actual Output: {result}')
    if result == expected:
        print('Status: Passed')
    else:
        print('Status: Failed')

"""
    EXPECTED OUTPUT:
    ----------------
    Test 1
    Input: []
    Expected Output: []
    Actual Output: []
    Status: Passed
    
    Test 2
    Input: [1]
    Expected Output: [1]
    Actual Output: [1]
    Status: Passed
    
    Test 3
    Input: [1, 2, 3, 4, 5]
    Expected Output: [1, 2, 3, 4, 5]
    Actual Output: [1, 2, 3, 4, 5]
    Status: Passed
    
    Test 4
    Input: [1, 2, 2, 1, 3, 3, 3, 2, 2]
    Expected Output: [1, 2, 2, 2, 3, 3, 3, 3, 3]
    Actual Output: [1, 2, 2, 2, 3, 3, 3, 3, 3]
    Status: Passed
    
    Test 5
    Input: [-1, -2, -3, -4, -5]
    Expected Output: [-1, -1, -1, -1, -1]
    Actual Output: [-1, -1, -1, -1, -1]
    Status: Passed

"""
