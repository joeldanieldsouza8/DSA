from enum import Enum


class PivotStrategy(Enum):
    LAST = 0
    MEDIAN = 1
    RANDOM = 3


class PartitionScheme(Enum):
    NAIVE = 0
    LOMUTO = 1
    HOARE = 2


def swap_values(nums: list[int], index_1: int, index_2: int) -> None:
    nums[index_1], nums[index_2] = nums[index_2], nums[index_1]


def partition(nums: list[int], low_index: int, high_index: int) -> int:
    pivot = nums[high_index]

    partition_index = low_index

    for current_index in range(low_index, high_index):
        # Check if the value of the current element is less than the value of the element at the pivot
        if nums[current_index] <= pivot:
            swap_values(nums, current_index, partition_index)
            partition_index += 1  # Move the partition marker

    # Swap the element at the pivot with the 'partition_index'
    swap_values(nums, partition_index, high_index)

    return partition_index


def quick_sort(nums: list[int], low_index: int, high_index: int):
    # Check if there are at least two elements to sort
    if low_index >= high_index:
        return

    partition_index = partition(nums, low_index, high_index)

    # Sort the left-subarray
    quick_sort(nums, low_index, partition_index - 1)

    # Sort the right-subarray
    quick_sort(nums, partition_index + 1, high_index)


arr = [10, 15, 25, 30, 17]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted list:", arr)  # Output: [10, 15, 17, 25, 30]
