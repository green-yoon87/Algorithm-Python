import sys 
num = int(sys.stdin.readline())

def solution(num):
    stack = []
    top = -1
    for i in range(num):
        line = sys.stdin.readline()
        inputs = line.split()
        if inputs[0] == "pop":
            if len(stack) > 0:
                print(stack.pop())
            else:
                print(-1)
        elif inputs[0] == "top":
            if len(stack) >= 1:
                element = stack.pop()
                print(element)
                stack.append(element)
            elif len(stack) == 0:
                print(-1)
        elif inputs[0] == "size":
            print(len(stack))
        elif inputs[0] == "empty":
            if stack:
                  print(0)
            else:
                  print(1)
        elif inputs[0] == "push":
            num = int(inputs[1])
            stack.append(num)  

solution(num)  