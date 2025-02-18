def bubble_sort(nums: list[int]):
    n = len(nums)

    # The outer loop will do n passes through the entire list. Eg, if n=6 (the length of the list), do 6 passes through the entire list
    for i in range(n):
        # This is used to track whether any swaps happen in a given pass. If no swaps occur in a given full pass, it means the list is already sorted, and we can stop early instead of continuing with further unnecessary passes through the list.
        swapped = False

        # The inner loop will swap the values, based on the condition, for the current pass through the list
        # With each pass, the traversal through the (entire) list reduces by 1 because the elements towards the end of the list are sorted
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        # Exit out of the loop early, if no swap has occurred during a given pass through the list
        if not swapped:
            break

    # Return the sorted list
    return nums


print(bubble_sort([4, 2, 6, 5, 1, 3]))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]

 """
