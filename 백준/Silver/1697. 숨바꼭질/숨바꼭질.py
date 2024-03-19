import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
group = [[] for _ in range(1000001)]
visited = [False for _ in range(1000001)]

for i in range(1000001):
    if i> 0:
        group[i].append(i-1)
    if i< (100000):
        group[i].append(i+1)
    if i * 2 <= 100000:
        group[i].append(i*2)
def bfs(group, node, visited):
    queue = deque([(node, 0)])
    visited[node] =True
    while queue:
        popNode = queue.popleft()
        value, depth = popNode[0], popNode[1]
        if value == k:
            return depth
        for c in group[value]:
            if not visited[c]:
                queue.append((c, depth+1))
                visited[c] = True
print(bfs(group, n, visited))
    