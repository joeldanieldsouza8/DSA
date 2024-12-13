class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list) - 1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

# Return a new string with the letters in reverse order
# Time Complexity: O(n) - As we have to iterate over each character in the string
# Space Complexity: O(1)
def reverse_string(string: str) -> str:
    # Check if the string is empty
    if len(string) == 0:
        return string

    reversed_string = ""

    for char in reversed(string):
        reversed_string += char

    return reversed_string


my_string = 'hello'

print(reverse_string(my_string))

"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""
