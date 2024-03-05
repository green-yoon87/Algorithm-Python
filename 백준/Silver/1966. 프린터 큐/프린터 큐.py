import sys
from collections import deque

input = sys.stdin.readline
num = int(input())
q = deque()
answer = []
for i in range(num):
    q = deque()
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    for i in range(len(priority)):
        q.append((priority[i], i))

    order = 0
    
    maximum = max(q)[0]
    while q:
        element = q.popleft()
        if maximum > element[0]:
            q.append(element)
        else:
            order += 1
            if element[1] == m:
                break
            else:
              if q:
                maximum = max(q)[0]
    print(order)
    
    