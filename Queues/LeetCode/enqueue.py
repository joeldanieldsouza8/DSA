class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def __str__(self):
        return f"stack1: {self.stack1}, stack2: {self.stack2}"

    def enqueue(self, value: int):
        # Transfer all elements from 'stack1' to 'stack2'
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        # Add the new element to 'stack1'
        self.stack1.append(value)

        # Transfer elements back from stack2 to stack1. The purpose of this is so that the first element added to the list is at the end of the list (i.e. the front of the queue)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0


# Create a new queue
q = MyQueue()

# Enqueue some values
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Output the front of the queue
print("Front of the queue:", q.peek())

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())

"""
    EXPECTED OUTPUT:
    ----------------
    Front of the queue: 1
    Is the queue empty? False

"""

"""
    START:
    ----------------
    [1, 2, 3]
    
    END:
    ----------------
    [3, 2, 1]
"""
