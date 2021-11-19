# Reverse an string

from _collections import deque

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

def reverse_string(s):
    stack = Stack()

    for char in s:
        stack.push(char)

    string_reverse = ''

    while stack.size() != 0:
        string_reverse += stack.pop()

    return string_reverse

if __name__ == '__main__':
    st1 = "We will conquere COVID-19"
    print("The reverse of ", st1, "is: \n", reverse_string(st1))
