import sys
input = sys.stdin.readline

num = int(input())
numArr = list(map(int, input().split()))
numArr = [(i, idx) for idx, i in enumerate(numArr)]      
numArr.sort()
temp, minimum = 0, 0 
for i in range(len(numArr)):
    if i == 0:
        minimum = numArr[i][0]
    if numArr[i][0] > minimum:
        temp +=1
        minimum = numArr[i][0]
    numArr[i] = (temp, numArr[i][1])

numArr.sort(key = lambda x:x[1])
for i in numArr:
    print(i[0], end=" ")
          