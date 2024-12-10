class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.next: Node | None = None


class Stack:
    def __init__(self, value: int):
        new_node = Node(value)
        self.top: Node | None = new_node
        self.height: int = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        # Check if there are any nodes in the stack
        if self.height == 0:
            return None

        removed_node: Node | None = self.top

        # Check if there is only one node in the stack
        if self.height == 1:
            self.top = None

        else:
            self.top = self.top.next
            removed_node.next = None

        self.height -= 1
        return removed_node

my_stack = Stack(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)

print('Stack before pop():')
my_stack.print_stack()

print('\nPopped node:')
print(my_stack.pop().value)

print('\nStack after pop():')
my_stack.print_stack()

"""
    EXPECTED OUTPUT:
    ----------------
    Stack before pop():
    1
    2
    3
    4

    Popped node:
    1

    Stack after pop():
    2
    3
    4

"""