def find_longest_string(fruits: list[str]):
    longest: str = ""

    for fruit in fruits:
        if len(fruit) > len(longest):
            longest = fruit

    return longest    


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""