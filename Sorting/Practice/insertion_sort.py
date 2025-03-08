def insertion_sort(nums: list[int]):
    n = len(nums)

    # Iterate through the list starting from the second element. The assumption is that the first element at i=0 is already sorted
    for i in range(1, n):
        key = nums[i]  # Element to be inserted into the sorted portion
        j = i - 1  # Start comparing with the previous element

        # Shift elements to the right until the correct position for the key is found
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]  # Shift element one step to the right
            j -= 1  # Move left in the list

        # Place the key at its correct position
        nums[j + 1] = key

    return nums


print(insertion_sort([4, 2, 6, 5, 1, 3]))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]

 """
