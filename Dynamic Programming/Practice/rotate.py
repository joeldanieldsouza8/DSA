def rotate(nums: list[int], k: int):
    n = len(nums)

    # Check if the list is empty or there is only one element, which means there is no need to do anything.
    # Check if k = 0, which means there is no need to do anything.
    if (n < 2) or (k == 0):
        return

    # Ensures that the value of k is always within the range of 0 and N-1
    k = k % n

    # Private function to swap elements in the list.
    def swap(nums: list[int], start_index: int, end_index: int):
        # start_index = 0
        # end_index = len(nums) - 1

        # Continue the loop as long as the 'start' pointer hasn't crossed (or surpassed) the 'end' pointer or the 'start' and 'end' pointer are not at the same index position (which would be the case with odd number of elements in the list).
        while start_index <= end_index:
            # Swap the nums
            nums[start_index], nums[end_index] = nums[end_index], nums[start_index]

            # Update the pointers
            start_index += 1  # Move the 'start' pointer towards the right of the list.
            end_index -= 1  # Move the 'end' pointer towards the left of the list.

    # e.g., when k = 3.

    # Step 1: Reverse the entire list
    # e.g., [1,2,3,4,5,6,7] -> [7,6,5,4,3,2,1]
    swap(nums, 0, n - 1)

    # Step 2: Reverse the first k elements
    # e.g., [7,6,5, | 4,3,2,1] -> [5,6,7, | 4,3,2,1]
    swap(nums, 0, k - 1)

    # Step 3: Reverse the remaining n-k elements
    # e.g., [5,6,7, | 4,3,2,1] -> [5,6,7, | 1,2,3,4]
    swap(nums, k, n - 1)


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)

"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""
