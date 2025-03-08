def merge(nums_1: list[int], nums_2: list[int]):
    combined = []
    i = j = 0

    while i < len(nums_1) and j < len(nums_2):
        if nums_1[i] < nums_2[j]:
            combined.append(nums_1[i])
            i += 1
        else:
            combined.append(nums_2[j])
            j += 1

    combined += nums_1[i:]
    combined += nums_2[j:]

    return combined


def merge_sort(nums: list[int]):
    # Base case: Check if the length of the list is 1, return the list as it is already sorted.
    if len(nums) == 1:
        return nums

    # Continue dividing (i.e., breaking) the list in half.
    middle_index = len(nums) // 2
    left_sorted_list = merge_sort(
        nums[:middle_index])  # Note: Here we pass a new list each time. Every recursive call returns a sorted list.
    right_sorted_list = merge_sort(
        nums[middle_index:])  # Note: Here we pass a new list each time. Every recursive call returns a sorted list.

    # Merge the sorted halves into a new list
    merged_list = merge(left_sorted_list, right_sorted_list)

    return merged_list


print(merge([1, 2, 7, 8], [3, 4, 5, 6]))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8]

 """

original_list = [3, 1, 4, 2]

sorted_list = merge_sort(original_list)

print('Original List:', original_list)

print('\nSorted List:', sorted_list)

"""
    EXPECTED OUTPUT:
    ----------------
    Original List: [3, 1, 4, 2]

    Sorted List: [1, 2, 3, 4]

 """
