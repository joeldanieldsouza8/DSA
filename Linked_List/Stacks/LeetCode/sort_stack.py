from typing import List


class Stack:
    def __init__(self):
        self.stack_list = []

    def __str__(self):
        return f"{self.stack_list}"

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

# Sort the elements in the stack in ascending order (the lowest value will be at the top of the stack) using only one additional stack
# Time Complexity: O(n^2) - As we have a nested loop
# Space Complexity: O(n) - As we are using a temporary stack to hold 'n' elements
def sort_stack(input_stack: Stack):
    temp_stack: Stack = Stack()

    while not input_stack.is_empty():
        # Pop the top element from the input stack
        temp = input_stack.pop()

        # Move elements from temp_stack back to input_stack if they are greater than temp
        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            input_stack.push(temp_stack.pop())

        # Push the current element into the temp_stack
        temp_stack.push(temp)

    # Move the elements back to input_stack to maintain ascending order
    while not temp_stack.is_empty():
        input_stack.push(temp_stack.pop())

    return input_stack

my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2) # top of the stack

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()

"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""
