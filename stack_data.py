class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if not self.stack:
            return True
        return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)


def balance_check(data):
    view_bracket = {'(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{'}
    stack = Stack()

    for bracket in data:
        if stack.isEmpty() or view_bracket[bracket] != stack.peek():
            stack.push(bracket)
        else:
            stack.pop()
    
    if stack.isEmpty():
        return 'сбалансированная последовательность'
    else:
        return 'несбалансированная последовательность'