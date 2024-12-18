# This implementation passes the test, but will fail when the values fall outside the range 0-9
# def item_in_common(list1: list[int], list2: list[int]):
#     common_dict = {
#         0: 0,
#         1: 0,
#         2: 0,
#         3: 0,
#         4: 0,
#         5: 0,
#         6: 0,
#         7: 0,
#         8: 0,
#         9: 0,
#     }
#
#     for num in list1:
#         if common_dict.get(num) == 0:
#             common_dict[num] = 1
#
#     for num in list2:
#         if common_dict.get(num) > 0:
#             return True

def item_in_common(list1: list[int], list2: list[int]):
    # Create a dictionary to store elements from the first list
    elements = {}

    # Add all elements of list1 to the dictionary
    for item in list1:
        elements[item] = True

    # Check if any element of list2 exists in the dictionary
    for item in list2:
        if item in elements:
            return True

    return False

list1 = [1,3,5]
list2 = [2,4,5]


print(item_in_common(list1, list2))



"""
    EXPECTED OUTPUT:
    ----------------
    True

"""