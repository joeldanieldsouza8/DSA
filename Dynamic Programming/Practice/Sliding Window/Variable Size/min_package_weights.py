import math


def min_package_weights(package_weights: list[int], min_weight: int) -> float:
    # Check if the list is empty
    if not package_weights:
        return 0

    # Store the index position of the element at the start of the window
    start_pointer = 0  
    
    # Store the index position of the current element in the list
    # end_pointer = 0

    # Store the sum of all elements in the window
    current_window_sum = 0  

    # Initialise to positive infinity. If 0 was initialised it would always be the minimum
    best_min_length = math.inf 

    # Iterate through the entire list, until the end of the list is reached
    for end_pointer in range(len(package_weights)):
        # Expand the window by adding the current element to the right of the window
        current_window_sum += package_weights[end_pointer]

        # Shrink the window from the start, until the sum in the window is greater than or equal to the min weight
        while current_window_sum >= min_weight:
            # Update the size of the current window
            current_window_length = (end_pointer - start_pointer) + 1

            # Update the best min length to check if there are fewer elements in the list that can meet the requirement for the min weight
            best_min_length = min(best_min_length, current_window_length)

            # Remove the element at the start of the window
            current_window_sum -= package_weights[start_pointer]

            # Shrink the window from the start
            start_pointer += 1

    # Check if there were any items that met the min length
    return best_min_length if best_min_length != math.inf else 0


# print(min_package_weights(package_weights=[2, 3, 1, 2, 4, 3], min_weight=7))
# # Expected Output: 2, because [4, 3]

# # Test Case 2: No possible solution
# print(min_package_weights(package_weights=[1, 1, 2, 1, 3], min_weight=10))
# # Expected Output: 0, because 1 + 1 + 2 + 1 + 3 = 8

# Test Case 3: Single package weight suffices
print(min_package_weights(package_weights=[3, 4, 1, 1, 12, 2, 8], min_weight=11))
# Expected Output: 1, because [12]
