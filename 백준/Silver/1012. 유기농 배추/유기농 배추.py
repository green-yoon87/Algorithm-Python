import sys
from collections import deque

input = sys.stdin.readline
num = int(input())
matrix = []
visited = []

def dfs(matrix, m, n, x, y, visited):
    answer = 0
    q = deque()
    if matrix[y][x] == 1 and not visited[y][x]: 
        q.append((y, x))
        visited[y][x] = True
    while q:
        popNode = q.popleft()
        answer +=1
        i, j = popNode[0], popNode[1]
        if i>0 and matrix[i-1][j] == 1 and not visited[i-1][j]:
            q.append((i-1, j))
            visited[i-1][j] = True
        if j>0 and matrix[i][j-1] == 1 and not visited[i][j-1]:
            q.append((i, j-1))
            visited[i][j-1] = True
        if j<m-1 and matrix[i][j+1] == 1 and not visited[i][j+1]:
            q.append((i, j+1))
            visited[i][j+1] = True
        if i<n-1 and matrix[i+1][j] == 1 and not visited[i+1][j]:
            q.append((i+1, j))
            visited[i+1][j] = True
    return answer

answer = []
for _ in range(num):
    m, n, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]
    visited = [ [False] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        matrix[y][x] = 1 # 배추 있는 곳 
    count = 0
    for i in range(m):
        for j in range(n):
            value = dfs(matrix, m, n, i, j, visited)
            if value > 0:
                count +=1
    answer.append(count)
for i in answer:
    print(i)