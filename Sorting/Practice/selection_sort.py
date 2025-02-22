def selection_sort(nums: list[int]):
    n = len(nums)

    # Iterate through the list, moving the boundary of the sorted section
    for i_index in range(n - 1):
        # Assume the first element in the unsorted section is the minimum
        min_index = i_index

        # With each pass, the previous index position contains the sorted element. So, we don't need to go through the entire list again. Hence, iterate over only the remaining unsorted elements to find the smallest value
        for j_index in range(i_index + 1, n):
            # Update min_index if a smaller element is found
            if nums[j_index] < nums[min_index]:
                min_index = j_index

        # Swap only if a smaller element was found
        if min_index != i_index:
            # After a given pass through part of the list is done, swap the element at the current index position with the element at the 'min_index'
            nums[i_index], nums[min_index] = nums[min_index], nums[i_index]

    return nums


print(selection_sort([4, 2, 6, 5, 1, 3]))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]

 """
