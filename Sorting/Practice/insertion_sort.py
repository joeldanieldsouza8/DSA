def insertion_sort(nums: list[int]):
    n = len(nums)

    # Iterate through the list starting from the second element
    for i in range(1, n):
        key = nums[i]  # Element to be inserted into the sorted portion
        j_index = i - 1  # Start comparing with the previous element

        # Shift elements to the right until the correct position for key is found
        while j_index >= 0 and nums[j_index] > key:
            nums[j_index + 1] = nums[j_index]  # Shift element one step to the right
            j_index -= 1  # Move left in the list

        # Place the key at its correct position
        nums[j_index + 1] = key

    return nums


print(insertion_sort([4, 2, 6, 5, 1, 3]))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]

 """
