from typing import List
from typing import Dict

# Incorrect Implementation

# def twoSum(nums: List[int], target: int) -> List[int]:
#     # Check if the list is empty
#     if nums is None:
#         return []

#     hash_map: Dict[int, int] = dict()

#     for index, element in enumerate(nums):
#         difference = target - element # 7 - 3 = 4 | 7 - 4 = 3
        
#         # Check if the element (key) doesn't exist in the hash map
#         if element not in hash_map:
#             hash_map[element] = index # {3 : 0, 4 : 1}
#             # hash_map[element] = hash_map.get(index, 0)

#         # print(f"hash_map[{element}] -----------> {hash_map[element]}")
#         # print(f"hash_map[{difference}] -----------> {hash_map[difference]}")

#         if difference + hash_map[element] == target:
#             return [hash_map[difference], hash_map[element]]



# ==================================================



# Correct Implementation

# Objective: Find the first pair whose sum equals the target.

def twoSum(nums: List[int], target: int) -> List[int]:
    # Check if the list is empty
    if nums is None:
        return []

    seen: Dict[int, int] = dict()

    for current_index, current_number in enumerate(nums):
        # The `complement` (or `remaining`, `difference`) variable asks the question, "What number do I need to find to make the `target`?"
        # target = a + b, 
        #   where:
        #       a is the complement 
        #       b is the is the current_number 
        complement = target - current_number 

        # Check if the `complement` number (key) was seen previously (or already exists in the hash map)
        if complement in seen:
            previous_index = seen[complement]

            return [previous_index, current_index]

        # Otherwise, add the `current_number` to `seen` for future checks
        seen[current_number] = current_index



# --- TEST CASES ---

def run_test(test_name: str, nums: List[int], target: int, expected_result: List[int]):
    result = twoSum(nums, target)

    status = "✅ PASS" if result == expected_result else f"❌ FAIL (Expected {expected_result})"

    print(f"--- {test_name} ---")
    print(f"Input: {nums}, Target: {target}")
    print(f"Result: {result} | {status}")
    print("\n------------------------------------------------\n")


run_test("The Standard", [2, 11, 7, 15], 9, [0, 2])

run_test("The Twins", [3, 2, 4, 3], 6, [1, 2])

run_test("The Negatives", [-1, -2, -3, -4, -5], -8, [2, 4])

run_test("The Zero", [0, 4, 3, 0], 0, [0, 3])

run_test("The Long Walk", [1, 5, 5, 11, 10], 11, [0, 4])