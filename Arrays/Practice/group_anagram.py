from typing import List

# Time Complexity: O(N * K(log(K)))
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # Check if the list is empty
    if not strs:
        return []
    
    anagram_map: dict[tuple[str, ...], list[str]] = {}

    for word in strs:
        # Sort the characters in the word in alphabetical order, and wrap it in a tuple to make the 'key' immutable and hashable 
        sorted_word = tuple(sorted(word))

        # If the sorted word doesn't yet exist in the dictionary, then initialise it with an empty list as its 'key'
        if sorted_word not in anagram_map:
            anagram_map[sorted_word] = []

        # Append the word to the list in the 'value' 
        anagram_map[sorted_word].append(word)

    return list(anagram_map.values())




print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))