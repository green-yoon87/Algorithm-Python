import sys
import heapq

input = sys.stdin.readline
heap = []
num = int(input())

for i in range(num):
    element = -1 *int(input())
    if element ==0:
        if len(heap) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(heap))
    else:
        heapq.heappush(heap, element)