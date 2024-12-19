def find_pairs(arr1: list[int], arr2: list[int], target: int):
    unique_arr1 = set(arr1)
    pairs = []

    for num in arr2:
        complement = target - num

        if complement in unique_arr1:
            pairs.append((complement, num))

    return pairs


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print(pairs)

"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""
