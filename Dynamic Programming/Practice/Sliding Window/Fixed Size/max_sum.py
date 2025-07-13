"""
The problem with this solution is:
    - Re-computes the sum for each sub-array every time which is a redundant and wasted operation.

    - Only works for k=3.
"""
# def max_sum(nums: list[int], k: int) -> int:
#     # Check if there are no elements in the list
#     if not nums:
#         return 0
    
#     # Check if there are at least k elements in the list
#     if len(nums) < k:
#         return 0
    
#     # prev_start_sub_array  = 0
#     start_sub_array_index = 0
#     middle_sub_array_index = 1
#     end_sub_array_index = 2

#     max_sum = 0

#     while end_sub_array_index < len(nums):
#         # curr_sum = nums[start_sub_array_index] + nums[middle_sub_array_index] + nums[end_sub_array_index] - prev_start_sub_array

#         curr_sum = nums[start_sub_array_index] + nums[middle_sub_array_index] + nums[end_sub_array_index] 

#         max_sum = max(max_sum, curr_sum)

#         # prev_start_sub_array = nums[start_sub_array_index]
#         start_sub_array_index += 1
#         middle_sub_array_index += 1
#         end_sub_array_index += 1

#     return max_sum


def max_sum(nums: list[int], k: int) -> int:
    if (not nums) or (len(nums) < k):
        return 0
    
    # Initialise the value of 'window_sum' to the sum of the first k elements in the list.
    window_sum = sum(nums[0:k])

    # Stores the maximum sum we have seen so far.
    max_sum = window_sum

    for i in range(k, len(nums)):
        entering_element = nums[i]
        leaving_element = nums[i - k] # The element leaving is k positions behind the entering element

        # Calculates the sum of the current sub-array
        window_sum = window_sum + entering_element - leaving_element

        max_sum = max(max_sum, window_sum)

    return max_sum


# Test Cases

# Test Case 1
print(max_sum([2, 1, 5, 1, 3, 2], 3))
# Output Subarray: [5, 1, 3]
# Expected Maximum Sum: 9

# Test Case 2
print(max_sum([-2, 10, -5, 8, -1, 4], 3))
# Output Subarray: [10, -5, 8]
# Expected Maximum Sum: 13

# Test Case 3
print(max_sum([1, 2, 3, 4, 5], 5))
# Output Subarray: [1, 2, 3, 4, 5]
# Expected Maximum Sum: 15