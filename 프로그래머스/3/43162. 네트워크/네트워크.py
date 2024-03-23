from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for c in range(n):
        value = bfs(c, computers, visited)
        if value:
            answer +=1
    return answer

def bfs(node, computers, visited):
    network = False
    q = deque([])
    if not visited[node]:
        q.append(node)
        visited[node] = True
        network = True
    while q:
        popNode = q.popleft()
        for c in range(len(computers[popNode])):
            if not visited[c] and computers[popNode][c] == 1:
                q.append(c)
                visited[c] = True
    return network    
    