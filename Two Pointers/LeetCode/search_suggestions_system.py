"""
Constraints:
    1. The words in the 'products' list is unique.
    2. Every word in the 'products' list and 'searchWord' is in lowercase english alphabets.
    3. Assume the 'products' list is unsorted.

Algorithm:
    - Narrow down the 'products' list character by character.
"""

def suggestedProducts(products: list[str], searchWord: str) -> list[list[str]]:
    # products = ["mobile","mouse","moneypot","monitor","mousepad"]
    # searchWord = "mouse"

    # Check if the 'products' list is empty
    # If the 'products' list is empty, it means there are no products to search for
    if not products:
        return []

    # Length of the 'searchWord' string
    n: int = len(searchWord) # n = 5

    # Sort the original 'products' list in-place, in lexographical order
    # This ensures that words with the same prefix are always grouped together. For example, 
    products.sort() # products = ["mobile","moneypot","monitor","mouse","mousepad"]

    # Initialise the output list to return at the end
    all_suggestions: list[list[str]] = []

    # Initialise the two pointers
    left = 0 # "mobile"
    right = len(products) - 1 # "mousepad"

    # Iterate through the 'searchWord' string
    # searchWord = "mouse"
    #               |||||
    # Index:        01234
    for index, letter in enumerate(searchWord): 
        while left <= right: # If 'left' > 'right', it means the poiinters have crossed and no words match
            # Check if the current 'index' is greater than, the last valid index of the word that the 'left' pointer is currently pointing to. This condition comes first because ... 
            # Check if the current 'letter' at this specific position in the word that the 'left' pointer is currently pointing to, matches the current 'letter' 
            # If either of these conditions fail, it means the current word that the 'left' pointer is currently pointing to is "bad" and discarded
            if (index > (len(products[left]) - 1)) or (letter != products[left][index]):
                left += 1

            else:
                break

        while left <= right:
            if (index > (len(products[right]) - 1)) or (letter != products[right][index]):
                right -= 1

            else:
                break

        # For this current iteration the "window" is in the correct place or the "window" is now valid
        # Take the top three words from the left-side of the "window"
        current_matches: list[str] = products[left : min(left + 3, right + 1)] # [start : stop], 'stop' if there are less than 3 words in the window get the minimum
        all_suggestions.append(current_matches)

    return all_suggestions
        






# print(suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"],"mouse"))
# print(suggestedProducts(["havana"], "havana"))
print(suggestedProducts(["bags","baggage","banner","box","cloths"], "bags"))