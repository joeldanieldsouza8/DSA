# # Without using the '.max' method
# def max_subarray(nums: list[int]) -> int:
#     # Check if there are no elements in the list
#     if not nums:
#         return 0

#     max_sum_so_far = nums[0]
#     curr_max = nums[0]

#     for i in range(1, len(nums)):
#         num = nums[i]

#         # Stores the sum of the current sub-array.
#         # Note, it's important to recognise that element 'num' at the current index position is considered as a single sum in itself.
#         sum_sub_array = curr_max + num

#         # Check if the value of the current 'num' (which is a sum in itself) is greater than the value of the current max.
#         # If so, a new sub-array is created as there could be a better sum.
#         if num > sum_sub_array:
#             curr_max = num
#         else:
#             curr_max = sum_sub_array

#         # Check if the current sum is greater than the max sum so far.
#         # If so, a new max sum has been found.
#         if curr_max > max_sum_so_far:
#             max_sum_so_far = curr_max
         
#     return max_sum_so_far
    


# Using the '.max' method
def max_subarray(nums: list[int]) -> int:
    # Check if there are no elements in the list
    if not nums:
        return 0

    max_sum_so_far = nums[0] # Stores the max sum found so far
    curr_max = nums[0] # Stores the current max sum found based on processing a sub-array

    for i in range(1, len(nums)):
        num = nums[i]
        
        curr_max = max(curr_max + num, num)

        max_sum_so_far = max(max_sum_so_far, curr_max)

    return max_sum_so_far


# Example 1: Simple case with positive and negative numbers
input_case_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result_1 = max_subarray(input_case_1)
print("Example 1: Input:", input_case_1, "\nResult:", result_1)

# Example 2: Case with a negative number in the middle
input_case_2 = [1, 2, 3, -4, 5, 6]
result_2 = max_subarray(input_case_2)
print("Example 2: Input:", input_case_2, "\nResult:", result_2)

# Example 3: Case with all negative numbers
input_case_3 = [-1, -2, -3, -4, -5]
result_3 = max_subarray(input_case_3)
print("Example 3: Input:", input_case_3, "\nResult:", result_3)

"""
    EXPECTED OUTPUT:
    ----------------
    Example 1: Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
    Result: 6
    Example 2: Input: [1, 2, 3, -4, 5, 6] 
    Result: 13
    Example 3: Input: [-1, -2, -3, -4, -5] 
    Result: -1

"""