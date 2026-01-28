def isValid(s: str) -> bool:
    # Check if the string is empty
    if not s:
        return False
    
    unmatched_openers: list[str] = []

    expected_openers:dict[str, str] = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in s:
        # Check if the 'char' is a closing bracket
        if char in expected_openers:
            # Check if the stack is empty
            if not unmatched_openers:
                return False
            
            # Check if the corresponding opening bracket for this 'char' (which is a closing bracket) exists at the top of the stack
            if unmatched_openers.pop() != expected_openers[char]:
                return False

        # Otherwise, this 'char' is an opening bracket, so it is pending to be matched to its coressponding closing bracket
        else:
            unmatched_openers.append(char)
    
    # Valid only if there are no unmatched openers left in the stack. Because, for every open bracket there is its corresponding close bracket.
    return not unmatched_openers


print(isValid("()")) # True
print(isValid("()[]{}")) # True
print(isValid("(]")) # False
print(isValid("([])")) # True
print(isValid("([)]")) # False