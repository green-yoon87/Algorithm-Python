import sys
input = sys.stdin.readline

def isBalance(str):
    stack = []
    answer = "yes"
    for char in str:
        if char == '(' or char =='[':
            stack.append(char)
        elif char == ')':
            if stack:
                element = stack.pop()
                if element !='(':
                    answer = "no"
                    return answer 
            else:
                return "no"
                         
        elif char == ']':
            if stack:
                element = stack.pop()
                if element != '[':
                    answer = "no"
                    return answer
            else:
                return "no"
    if stack:
        answer = "no"
    return answer
    
while True:
    str = input().rstrip()
    if str == '.':
        break
    
    str = list(str)
    print(isBalance(str))
                