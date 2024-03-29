import sys
input = sys.stdin.readline
n = int(input())
timeList = []
for _ in range(n):
    start, end = map(int, input().split())
    timeList.append((start, end))
timeList.sort(key = lambda x: (x[1], x[0]))
prev, answer  = 0, 0
for i in timeList:
    start = i[0]
    if start >= prev:
        answer +=1
        prev = i[1]
print (answer)