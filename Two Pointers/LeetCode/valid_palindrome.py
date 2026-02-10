def isPalindrome(s: str) -> bool:
    # Check if the string is empty
    if not s:
        return False
    
    if s == " ":
        return True
    
    # Initialise the pointer variables
    left: int = 0
    right: int = len(s) - 1

    # Iterate through the list until the 'left' pointer has passed the 'right' pointer or the 'left' pointer is at the same position as the 'right' pointer
    while left <= right:
        # print(f"Left Pointer: {s[left]} ---> {type(s[left])}") # Debugging 
        # print(f"Right Pointer: {s[right]} ---> {type(s[right])}") # Debugging 
        
        if s[left].lower() == s[right].lower():
            left += 1
            right -= 1

        elif not s[left].isalnum():
            left += 1

        elif not s[right].isalnum():
            right -= 1

        else:
            return False
        
    return True





# print(isPalindrome("A man, a plan, a canal: Panama")) # True
# print(isPalindrome("race a car")) # False
# print(isPalindrome(" ")) # True
print(isPalindrome("0P")) # False