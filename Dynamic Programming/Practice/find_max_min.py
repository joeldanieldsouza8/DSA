# Returns a tuple: (max_value, min_value)

def find_max_min(nums: list[int]) -> tuple[int, int]:
    min_index: int = 0
    max_index: int = 0
    
    for index in range(1, len(nums)):
        if nums[index] >= nums[max_index]:
            max_index = index

        elif nums[index] <= nums[min_index]:
            min_index = index

    return (nums[max_index], nums[min_index])



print(find_max_min([5, 3, 8, 1, 6, 9]))


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""
