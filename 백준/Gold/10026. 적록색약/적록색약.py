import sys
from collections import deque
input =sys.stdin.readline
graph = []
n = int(input())
visited = [[False] * n for _ in range(n)]
visited1 = [[False] * n for _ in range(n)]
for _ in range(n):
    alist = list(input().strip())
    graph.append(alist)
def bfs(node, visited):
    value = False
    q = deque([])
    if not visited[node[0]][node[1]]:
        q.append(node)
        visited[node[0]][node[1]] = True
        value = True
    while q:
        popNode = q.popleft()
        row, col, color = popNode[0], popNode[1], popNode[2]
        if row >0 and not visited[row-1][col] and graph[row-1][col] == color:
            q.append((row-1, col, color))
            visited[row-1][col] = True
        if col >0 and not visited[row][col-1] and graph[row][col-1] == color:
            q.append((row, col-1, color))
            visited[row][col-1] = True
        if row <n-1 and not visited[row+1][col] and graph[row+1][col] == color:
            q.append((row+1, col, color))
            visited[row+1][col] = True
        if col < n-1 and not visited[row][col+1] and graph[row][col+1] == color:
            q.append((row, col+1, color))
            visited[row][col+1] = True
    return value   
def specialBfs(node, visited):
    value = False
    q = deque([])
    if not visited[node[0]][node[1]]:
        q.append(node)
        visited[node[0]][node[1]] = True
        value = True
    while q:
        popNode = q.popleft()
        row, col, color = popNode[0], popNode[1], popNode[2]
        if row >0 and not visited[row-1][col]:
            if color == 'B':
                if graph[row-1][col] == color:
                    q.append((row-1, col, color))
                    visited[row-1][col] = True
            else:
                if graph[row-1][col] != 'B':
                    q.append((row-1, col, color))
                    visited[row-1][col] = True
            
        if col >0 and not visited[row][col-1]:
            if color == 'B':
                if graph[row][col-1] == color:
                    q.append((row, col-1, color))
                    visited[row][col-1] = True
            else:
                if graph[row][col-1] != 'B':
                    q.append((row, col-1, color))
                    visited[row][col-1] = True
        if row <n-1 and not visited[row+1][col]:
            if color == 'B':
                if graph[row+1][col] == color:
                    q.append((row+1, col, color))
                    visited[row+1][col] = True
            else:
                if graph[row+1][col] != 'B':
                    q.append((row+1, col, color))
                    visited[row+1][col] = True
        if col < n-1 and not visited[row][col+1]:
            if color == 'B':
                if graph[row][col+1] == color:
                    q.append((row, col+1, color))
                    visited[row][col+1] = True
            else:
                if graph[row][col+1] != 'B':
                    q.append((row, col+1, color))
                    visited[row][col+1] = True
    return value 
answer, answer1 = 0, 0    
for i in range(n):
    for j in range(n):
        if bfs((i,j, graph[i][j]), visited):
            answer+=1
        if specialBfs((i,j, graph[i][j]), visited1):
            answer1+=1
print(answer, answer1)
    