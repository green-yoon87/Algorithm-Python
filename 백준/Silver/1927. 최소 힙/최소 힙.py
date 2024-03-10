import sys
import heapq

input = sys.stdin.readline

num = int(input())
q = []

for i in range(num):
    element = int(input())
    if element == 0: 
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, element)