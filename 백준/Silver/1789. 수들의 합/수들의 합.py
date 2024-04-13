import sys
n = int(sys.stdin.readline())
answer = 0
sumNum = 0
num = 0
while sumNum != n:
    num +=1
    if sumNum + num > n:
      break 
    else:
        answer+=1
        sumNum += num 
print(answer)  