# Balance Parenthesis check

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

def is_match(char1, char2):
    match_dict = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    return match_dict[char1] == char2

def is_balanced(s):
    stack = Stack()

    for char in s:
        if char == '(' or char == '{' or char == '[':
            stack.push(char)
        if char == ')' or char == '}' or char ==']':
            if stack.size() == 0:
                return False
            if not is_match(char, stack.pop()):
                return False

    return stack.size() == 0

if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
