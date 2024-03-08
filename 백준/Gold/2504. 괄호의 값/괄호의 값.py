import sys
input = sys.stdin.readline

str = list(input().strip())
stack = []

def calculate(str):
    for char in str:
      if char == ')':
        number = 0
        while stack:
            element = stack.pop()
            if type(element) == int: # stack에 있는 문자가 정수형임을 확인
                number += element
                if not stack:
                    return 0
            elif element == '(':
                if number == 0:
                    number = 2
                else:
                    number *= 2
                stack.append(number)
                break
            else:
                return 0
        if number == 0: # 소괄호 짝이 맞지 않음
          return 0    
      elif char == ']':
        number = 0
        while stack: 
            element = stack.pop()
            if type(element) == int:
                number += element
                if not stack:
                    return 0
            elif element == '[':
                if number == 0:
                    number = 3
                else:
                    number *= 3
                stack.append(number)
                break
            else: # ')', '[', ']'이 나왔을 때 
                return 0 
        if number == 0:
            return 0 # 대괄호 짝이 맞지 않음

      else: # 문자가 '(' 이거나 '['일 때 
        stack.append(char)
    if '(' in stack or ')' in stack or '[' in stack or ']' in stack:
      return 0
    else:
      return sum(stack)

print(calculate(str))