import sys
input = sys.stdin.readline

num = int(input())

for i in range(num):
    stack = []
    cursorStack = []
    str = list(input().strip())
    for char in str:
        if char == '<':
            if stack:
                cursorStack.append(stack.pop())
        elif char == '>':
            if cursorStack:
                stack.append(cursorStack.pop())
        elif char == '-':
            if stack:
                stack.pop()
        else:
            stack.append(char)
    while cursorStack:
        stack.append(cursorStack.pop())
    print(''.join(stack ))
