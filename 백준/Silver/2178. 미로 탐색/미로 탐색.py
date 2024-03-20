import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
matrix = []
visited = [[False] * m for _ in range(n) ]

for _ in range(n):
    n_list = list(map(int, str(input().strip())))
    matrix.append(n_list)
    
def bfs(matrix, row, col, visited):
    q = deque([(row, col, 1)])
    visited[row][col]= True
    while q:
        popNode = q.popleft()
        row1, col1, depth1 = popNode[0], popNode[1], popNode[2]
        if row1 == n-1 and col1 == m-1:
            return depth1
        if row1 >0 and matrix[row1-1][col1] == 1 and not visited[row1-1][col1]:
            q.append((row1-1, col1, depth1 +1))
            visited[row1-1][col1] = True
        if col1 >0 and matrix[row1][col1-1] == 1 and not visited[row1][col1-1]:
            q.append((row1, col1-1, depth1 +1))
            visited[row1][col1-1] = True
        if row1 <n-1 and matrix[row1+1][col1] == 1 and not visited[row1+1][col1]:
            q.append((row1+1, col1, depth1 +1))
            visited[row1+1][col1] = True
        if col1 <m-1 and matrix[row1][col1+1] == 1 and not visited[row1][col1+1]:
            q.append((row1, col1+1, depth1 +1))
            visited[row1][col1+1] = True
        
print(bfs(matrix, 0, 0, visited))  