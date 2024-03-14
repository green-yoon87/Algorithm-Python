import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visitedDFS = [False] * (n+1) # 해당 노드를 방문했는지를 나타내는 배열
visitedBFS = [False] * (n+1) # 해당 노드를 방문했는지를 나타내는 배열

for i in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
for i in graph:
    i.sort()

def dfs(graph, node, visited):    
    visited[node] =True
    print(node, end = ' ')
    for i in graph[node]:
        if visited[i] == False:
            dfs(graph, i, visited)

def bfs(graph, node, visited):
    q = deque([node]) # bfs
    visited[node] = True
    
    while q:
        element = q.popleft()
        print(element, end =" ")
        for i in graph[element]:
            if not visited[i]:
                q.append(i)
                visited[i] = True            
        
dfs(graph, v, visitedDFS)
print()
bfs(graph, v, visitedBFS)