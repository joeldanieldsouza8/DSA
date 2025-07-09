"""
Time Complexity: O(n)
Space Complexity: O(1)

Constraints:
    - Re-arrange the original list in-place. DO NOT create a new list or use additional data structures. 
    - Unique elements are at the beginning of the list.

"""

# Two-pointer approach

def remove_duplicates(nums: list[int]):
    # Check if the list is empty
    if nums is None:
        return []

    # Assume the element at index 0 is unique
    seen_index = 1

    for index in range(1, len(nums)):
        # Keeps track of the index position of the most recent unique value in the list
        recent_unique_index = seen_index - 1

        if nums[index] != nums[recent_unique_index]:
            nums[seen_index] = nums[index] 

            seen_index += 1

    while seen_index < len(nums):
        nums.pop()

    return len(nums)
    


# # Test case 1: Empty list
# test1 = []
# print(f"Test 1 Before: {test1}")
# result1 = remove_duplicates(test1)
# print(f"Test 1 After: {test1[:result1]}")
# print(f"New Length: {result1}")
# print("------")

# # Test case 2: List with all duplicates
# test2 = [1, 1, 1, 1, 1]
# print(f"Test 2 Before: {test2}")
# result2 = remove_duplicates(test2)
# print(f"Test 2 After: {test2[:result2]}")
# print(f"New Length: {result2}")
# print("------")

# # Test case 3: List with no duplicates
# test3 = [1, 2, 3, 4, 5]
# print(f"Test 3 Before: {test3}")
# result3 = remove_duplicates(test3)
# print(f"Test 3 After: {test3[:result3]}")
# print(f"New Length: {result3}")
# print("------")

# Test case 4: List with some duplicates
test4 = [1, 1, 2, 2, 3, 4, 5, 5]
print(f"Test 4 Before: {test4}")
result4 = remove_duplicates(test4)
print(f"Test 4 After: {test4[:result4]}") # Expected Output: [1, 2, 3, 4, 5]
print(f"New Length: {result4}")
print("------")



