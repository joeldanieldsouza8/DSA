def lengthOfLongestSubstring(s: str) -> int:
    # Check if the string 's' is empty
    if not s:
        return 0

    # Initialise the two pointers
    left = 0 # Shrink from the left
    right = 0 # Grow from the right 

    best_length = 0
    current_length = 0

    seen: set[str] = set()

    # Iterate through each character in the string 's'
    for char in s:
        # # Check if the current 'character' has already been seen
        # if char in seen:
        #     # Remove the characters from the left side of the window, to "restart" the window
        #     while left < right:
        #         seen.clear()
        #         current_length -= 1
        #         left += 1

        # Check if the current 'character' has already been seen
        # Remove the characters from the left side of the window, until the duplicate character is removed from the window 
        # Note: We don't want to reset the window each time a duplicate character is found, we only want to ensure the window remains valid with non-duplicate characters. The entire goal of this problem is to find the longest contiguous sequence.
        while char in seen:
            # Remove the 'character' that the 'left' pointer is currently pointing to
            seen.remove(s[left])
            current_length -= 1
            left += 1

        # The current 'character' has not yet been seen
        # If the 'while' loop ran prior, it means we have successfully removed the "prior" duplicate 'character' from 'seen'. Add the current 'character' to 'seen' (which is the same 'character' that has just been removed from 'seen')
        seen.add(char)
        current_length += 1
        right += 1

        best_length = max(current_length, best_length)

    return best_length





# print(lengthOfLongestSubstring("abcabcbb"))
# print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("aab"))