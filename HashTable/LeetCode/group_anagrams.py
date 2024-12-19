def group_anagrams(words: list[str]):
    # Hash table to group words with the same length together
    anagrams = {}

    for word in words:
        # Sort the string to create a key
        sorted_key = ''.join(sorted(word))

        # Add the word to the corresponding group in the dictionary
        if sorted_key in anagrams:
            anagrams[sorted_key].append(word)

        else:
            anagrams[sorted_key] = [word]

    # Return the grouped anagrams as a list of values
    return list(anagrams.values())


print("1st set:")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

print("\n2nd set:")
print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

print("\n3rd set:")
print(group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]))

"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""
