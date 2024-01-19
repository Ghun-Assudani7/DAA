class StackArray:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.stack)


# Example Usage:
stack_array = StackArray()
stack_array.push(1)
stack_array.push(2)
stack_array.push(3)

print("Stack (Array) Peek:", stack_array.peek())
print("Stack (Array) Pop:", stack_array.pop())
print("Stack (Array) Size:", stack_array.size())
