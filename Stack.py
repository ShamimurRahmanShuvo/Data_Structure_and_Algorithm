# Stack using deque
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        if len(self.container) == 0:
            print("Stack is Empty")
        else:
            print("Stack has ", len(self.container), "elements")

    def size(self):
        return len(self.container)

if __name__ == '__main__':
    s = Stack()
    s.push(20)
    s.push(10)
    print(s.container)
    print(s.peek())
    s.is_empty()
    print(s.size())