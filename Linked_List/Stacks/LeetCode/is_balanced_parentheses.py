from typing import List


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


# The idea is to put all the opening brackets in the stack.
# Whenever you hit a closing bracket, search if the top of the stack is the opening bracket of the same nature.
# If this holds then pop the stack and continue the iteration. In the end if the stack is empty, it means all brackets are balanced or well-formed.
# Otherwise, they are not balanced.
def is_balanced_parentheses(parenthesis: str):
    """
    Check if the given string of parentheses is balanced.

    Time Complexity: O(n)
    Space Complexity: O(n)

    :param parenthesis: String containing parentheses.
    :return: True if balanced, False otherwise.
    """
    # Stack to keep track of opening parentheses
    temp_stack: List[str] = []

    for index, char in enumerate(parenthesis):
        # If not a closing bracket (which means it's an opening bracket), then push the current bracket to the stack
        if char == '(':
            temp_stack.append(char)

        # If the current bracket is a closing bracket, check if the bracket at the top of the stack is equal to the current bracket
        if char == ')':
            # Check if the stack is empty or the top is not matching
            if not temp_stack or temp_stack[-1] != '(':
                return False

            # Pop the matching opening parenthesis
            temp_stack.pop()

    # Return True if the stack is empty as all parenthesis are balanced and vice versa
    return len(temp_stack) == 0


def test_is_balanced_parentheses():
    try:
        assert is_balanced_parentheses('((()))') == True
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        assert is_balanced_parentheses('()') == True
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        assert is_balanced_parentheses('(()())') == True
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert is_balanced_parentheses('(()') == False
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert is_balanced_parentheses('())') == False
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        assert is_balanced_parentheses(')(') == False
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

    try:
        assert is_balanced_parentheses('') == True
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        assert is_balanced_parentheses('()()()()') == True
        print('Test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

    try:
        assert is_balanced_parentheses('(())(())') == True
        print('Test case 9 passed')
    except AssertionError:
        print('Test case 9 failed')

    try:
        assert is_balanced_parentheses('(()()())') == True
        print('Test case 10 passed')
    except AssertionError:
        print('Test case 10 failed')

    try:
        assert is_balanced_parentheses('((())') == False
        print('Test case 11 passed')
    except AssertionError:
        print('Test case 11 failed')


test_is_balanced_parentheses()

# is_balanced_parentheses('((()))')
