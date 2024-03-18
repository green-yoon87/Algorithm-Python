import sys
from collections import deque
input = sys.stdin.readline
matrix = []
n = int(input())
visited = [[0] * (n) for _ in range(n) ]

for _ in range(n):
    n_list = list(map(int, str(input().strip())))
    matrix.append(n_list)
answer = [] 

def search(matrix, x, y, visited):
    result = 0
    q = deque([])
    if not visited[x][y] and matrix[x][y] == 1:
        q.append((x,y))
        visited[x][y] = True
    while q:
        popNode = q.popleft()
        result +=1
        i = popNode[0]
        j = popNode[1]
        if i > 0 and not visited[i -1][j] and matrix[i-1][j] == 1:
            q.append((i-1, j))
            visited[i -1][j] = True
        if j > 0 and not visited[i][j-1] and matrix[i][j-1] == 1:
            q.append((i, j-1))
            visited[i][j-1] = True
        if i < n-1 and not visited[i +1][j] and matrix[i+1][j] == 1:
            q.append((i+1, j))
            visited[i+1][j] = True
        if j < n-1 and not visited[i][j+1] and matrix[i][j+1] == 1:
            q.append((i, j+1))
            visited[i][j+1] = True
    return result       

for i in range(n):
  for j in range(n):
      value = search(matrix, i, j, visited)
      if value >0:
          answer.append(value)
        
print(len(answer))
answer.sort()
for i in answer:
    print(i)
    