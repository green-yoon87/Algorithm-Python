import sys
from collections import deque
input = sys.stdin.readline

node, edge = map(int, input().split())
graph = [[] for _ in range(node+1)]
visited = [False] * (node +1)
for _ in range(edge):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

def search(graph, node, visited):
    answer = 0
    queue = deque()
    if not visited[node]:
        queue.append(node)
        visited[node] = True
    while queue:
        popNode = queue.popleft()
        answer +=1
        for c in graph[popNode]:
            if not visited[c]: 
                queue.append(c)
                visited[c] = True
    return answer
count = 0
for i in range(1, node+1):
    value = search(graph, i, visited)
    if value >= 1:
        count +=1

print(count)
        