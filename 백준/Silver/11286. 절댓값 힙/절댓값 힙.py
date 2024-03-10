import sys
import heapq

input = sys.stdin.readline
num = int(input())
heap = []
for i in range(num):
    element = int(input())
    if element == 0:
        if len(heap) == 0:
            print(0)
        else:
            popElement = heapq.heappop(heap)
            print(popElement[0]*popElement[1])
    else:
        if element<0:
            heapq.heappush(heap, (element * -1, -1))
        else:
            heapq.heappush(heap, (element, 1))