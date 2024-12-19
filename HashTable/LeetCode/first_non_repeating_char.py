def first_non_repeating_char(string: str):
    seen = {}

    # Count the frequency of each character
    for char in string:
        if char in seen:
            seen[char] += 1

        else:
            seen[char] = 1

    # Find the first character with a frequency of 1
    for char in string:
        if seen[char] == 1:
            return char

    return None

print(first_non_repeating_char('leetcode'))

print(first_non_repeating_char('hello'))

print(first_non_repeating_char('aabbcc'))

"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
