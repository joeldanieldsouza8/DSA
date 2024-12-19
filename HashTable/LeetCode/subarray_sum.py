def subarray_sum(nums: list[int], target: int):
    cumulative_sum_to_index = {} # Dictionary to store the cumulative sum and its index
    current_sum = 0 # Sum of all numbers up to the current index

    for index, num in enumerate(nums):
        current_sum += num

        # Check if the current cumulative sum equals the target
        if current_sum == target:
            # Subarray starts from index 0
            return [0, index]

        complement = current_sum - target

        # Check if the complement exists in the hash table
        if complement in cumulative_sum_to_index:
            start_index = cumulative_sum_to_index[complement] + 1
            return [start_index, index]

        # (Key: Value) cumulative_sum: index
        cumulative_sum_to_index[current_sum] = index

    # If no contiguous sub-array is found, return an empty list
    return []

nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))

nums = [-1, 2, 3, -4, 5]
target = 0
print(subarray_sum(nums, target))

nums = [2, 3, 4, 5, 6]
target = 3
print(subarray_sum(nums, target))

nums = []
target = 0
print(subarray_sum(nums, target))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
