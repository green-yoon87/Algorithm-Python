import sys
input = sys.stdin.readline
num = int(input())

def isVaild(strList):
    pair = 0
    for i in strList:
        if i == '(':
            pair +=1
        elif i == ')':
            pair -= 1
        
        if pair < 0:
            return "NO"
    if pair == 0:
        return "YES"
    else:
        return "NO"
            
        

for i in range(num):
    str = list(input())
    print(isVaild(list(str)))
            