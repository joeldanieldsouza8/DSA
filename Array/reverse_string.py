def reverse_string(letters: list[str]):
    start_index = 0
    end_index = len(letters) - 1

    # Continue the loop as long as the 'start' pointer hasn't crossed (or surpassed) the 'end' pointer.
    while start_index <= end_index:
        # Swap the letters
        letters[start_index], letters[end_index] = letters[end_index], letters[start_index]

        # Update the pointers
        start_index += 1 # Move the 'start' pointer towards the right of the list.
        end_index -= 1 # Move the 'end' pointer towards the left of the list.

    return letters

print(reverse_string(["h", "e", "l", "l", "o"]))
print(reverse_string(["j", "a", "s", "o", "n"]))
