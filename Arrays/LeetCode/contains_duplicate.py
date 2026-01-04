from typing import Set

def hasDuplicate(nums: List[int]) -> bool:
    # Check if the list is empty
    if not nums:
        return False

    seen : Set[int] = set()

    for num in nums:
        # Check if the current element exists in the set, which indicates that there is a repeating element in the list
        if num in seen:
            return True

        # Otherwise, add the current element to the set
        seen.add(num)

    # Otherwise, there are no repeating elements in the list
    return False


print(hasDuplicate([1,2,3,3]))
print(hasDuplicate([1,2,3,4]))