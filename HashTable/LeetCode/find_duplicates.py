# Approach 1
# def find_duplicates(nums: list[int]):
#     seen = {}
#     duplicates = set()
#
#     for num in nums:
#         if num in seen:
#             duplicates.add(num)
#
#         else:
#             seen[num] = True
#
#     return list(duplicates)

# Approach 2
def find_duplicates(nums: list[int]):
    seen = {} # Keeps track of the number of times a number is seen in the input list 'nums'
    duplicates = [] # Add all duplicate numbers in the required list format

    # Count the occurrences
    for num in nums:
        if num in seen:
            seen[num] += 1

        else:
            seen[num] = 1

    # Find duplicates
    for num, count in seen.items():
        if count > 1:
            duplicates.append(num)

    return duplicates


print(find_duplicates([1, 2, 3, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 3]))
print(find_duplicates([1, 1, 1, 1, 1]))
print(find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]))
print(find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))
print(find_duplicates([]))

"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""
