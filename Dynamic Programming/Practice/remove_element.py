# Two pointer technique (which uses the fast and slow pointer)

def remove_element(nums: list[int], value: int) -> int:
    # Keeps track of the current index position in the list as it scans through the list.
    read_index = 0
    
    # Keeps track of the index position where the element we want to keep should be placed.
    write_index = 0
    
    for read_index in range(len(nums)):
        if nums[read_index] != value:
            nums[write_index] = nums[read_index]
            
            write_index += 1

    while len(nums) > write_index:
        nums.pop()

    return len(nums)
    

# Test case 1: Removing a single instance of a value (1) in the middle of the list.
nums1: list[int] = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
val1 = 1
print("\nRemove a single instance of value", val1, "in the middle of the list.")
print("BEFORE:", nums1)
new_length1 = remove_element(nums1, val1)
print("AFTER:", nums1, "\nNew length:", new_length1)

# Original Length: 9
# Original List: [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Output Length: 7
# Output List: [-2, -3, 4, -1, 2, -5, 4]

print("-----------------------------------")

# Test case 2: Removing a value that's located at the end of the list.
nums2: list[int] = [1, 2, 3, 4, 5, 6]
val2 = 6
print("\nRemove value", val2, "that's located at the end of the list.")
print("BEFORE:", nums2)
new_length2 = remove_element(nums2, val2)
print("AFTER:", nums2, "\nNew length:", new_length2)

# Original Length: 6
# original List: [1, 2, 3, 4, 5, 6]

# Output Length: 5
# Output List: [1, 2, 3, 4, 5]

print("-----------------------------------")

# Test case 3: Removing a value that's located at the start of the list.
nums3: list[int] = [-1, -2, -3, -4, -5]
val3 = -1
print("\nRemove value", val3, "that's located at the start of the list.")
print("BEFORE:", nums3)
new_length3 = remove_element(nums3, val3)
print("AFTER:", nums3, "\nNew length:", new_length3)

# Original Length: 5
# original List: [-1, -2, -3, -4, -5]

# Output Length: 4
# Output List: [-2, -3, -4, -5]

print("-----------------------------------")

# Test case 4: Attempting to remove a value from an empty list.
nums4: list[int] = []
val4 = 1
print("\nAttempt to remove value", val4, "from an empty list.")
print("BEFORE:", nums4)
new_length4 = remove_element(nums4, val4)
print("AFTER:", nums4, "\nNew length:", new_length4)

# Original Length: 0
# original List: []

# Output Length: 0
# Output List: []

print("-----------------------------------")

# Test case 5: Removing all instances of a repeated value.
nums5: list[int] = [1, 1, 1, 1, 1]
val5 = 1
print("\nRemove all instances of value", val5, "from the list.")
print("BEFORE:", nums5)
new_length5 = remove_element(nums5, val5)
print("AFTER:", nums5, "\nNew length:", new_length5)

# Original Length: 5
# original List: [1, 1, 1, 1, 1]

# Output Length: 0
# Output List: []

print("-----------------------------------")

