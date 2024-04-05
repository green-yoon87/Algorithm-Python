import sys
from collections import deque
# x: 부모, y: 자식
input = sys.stdin.readline
num = int(input())
upGraph = [[] for _ in range(num+1)]
downGraph = [[] for _ in range(num+1)]
target1, target2 = map(int, input().split())
visited = [False for _ in range(num+1)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    downGraph[x].append(y)
    upGraph[y].append(x)
def bfs(node, target, visited):
    value = -1
    q = deque([(node, 0)])
    visited[node] = True
    while q:
        popNode = q.popleft()
        if popNode[0] == target:
            value= popNode[1]
            break
        for c in upGraph[popNode[0]]:
            if not visited[c]:
                q.append((c, popNode[1]+1))
                visited[c] = True
        for c in downGraph[popNode[0]]:
            if not visited[c]:
                q.append((c, popNode[1]+1))
                visited[c] = True
    return value
print(bfs(target1, target2, visited))
