# Approach 1: Using a for loop which is unnecessary
# def remove_duplicates(nums: list[int]):
#     unique = set()
#
#     for index, num in enumerate(nums):
#         if num not in unique:
#             unique.add(num)
#
#     return list(unique)

# Approach 2: Directly passing the list into the set
def remove_duplicates(nums: list[int]):
    unique_list = list(set(nums))
    return unique_list

my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)
print(new_list)



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    (Order may be different as sets are unordered)

"""