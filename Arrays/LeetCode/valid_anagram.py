from typing import Dict

def isAnagram(word_1: str, word_2: str) -> bool:
    # Check if both the strings aren't empty
    if (word_1 is None) or (word_2 is None):
        return False

    if len(word_1) != len(word_2):
        return False

    word_1_frequencies: Dict[str, int] = dict()
    word_2_frequencies: Dict[str, int] = dict()

    # # Iterate through all the characters in word_1
    # for char in word_1:
    #     if char not in word_1_frequencies:
    #         word_1_frequencies[char] = 1

    #     else:
    #         word_1_frequencies[char] += 1

    # Iterate through all the characters in word_1
    for char in word_1:
        word_1_frequencies[char] = word_1_frequencies.get(char, 0) + 1 # The LHS of the `=` reads as, "Get the value. If the bucket is empty, pretend it's 0. Now add 1."

    # # Iterate through all the characters in word_2
    # for char in word_2:
    #     if char not in word_2_frequencies:
    #         word_2_frequencies[char] = 1

    #     else:
    #         word_2_frequencies[char] += 1

    # Iterate through all the characters in word_2
    for char in word_2:
        word_2_frequencies[char] = word_2_frequencies.get(char, 0) + 1

    # for key, value in word_1_frequencies.items():
    #     # Check if the key in word_1_frequencies dict, does not exist in the word_2_frequencies dict
    #     if key not in word_2_frequencies:
    #         return False

    #     # # Check if the value of the corresponding key in word_2_frequencies dict is equal to the value of the corresponding key in word_1_frequencies
    #     # if word_2_frequencies[key] == value:
    #     #     continue

    #     # Check if the value of the corresponding key in word_2_frequencies dict is equal to the value of the corresponding key in word_1_frequencies
    #     if word_2_frequencies[key] != value:
    #         return False

    #     return False

    # return True

    return word_1_frequencies == word_2_frequencies # Python way, which replaced the verbose way in lines 38-53



print(isAnagram("racecar", "carrace")) # True
print(isAnagram("racecar", "carracey")) # False
print(isAnagram("racecar", "carracz")) # False