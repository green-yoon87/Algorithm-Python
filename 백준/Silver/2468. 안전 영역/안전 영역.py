import sys
input = sys.stdin.readline
n = int(input())
matrix = []
for _ in range(n):
    n_list = list(map(int, input().split()))
    matrix.append(n_list)
maximum = max(map(max, matrix))
minimum = min(map(min, matrix))
answer = []
def dfs(row, col, height):
    stack = []
    hasSafeArea = False
    if matrix[row][col] > height and not visited[row][col]:
        stack.append((row, col))
        visited[row][col] = True
        hasSafeArea = True
    while stack:
        popNode = stack.pop()
        i, j = popNode[0], popNode[1]
        if i > 0 and not visited[i-1][j] and matrix[i-1][j] > height:
            stack.append((i-1, j))
            visited[i-1][j] = True
        if j > 0 and not visited[i][j-1] and matrix[i][j-1] > height:
            stack.append((i, j-1))
            visited[i][j-1] = True
        if i < n-1 and not visited[i+1][j] and matrix[i+1][j] > height:
            stack.append((i+1, j))
            visited[i+1][j] = True
        if j < n-1 and not visited[i][j+1] and matrix[i][j+1] > height:
            stack.append((i, j+1))
            visited[i][j+1] = True
            
    return hasSafeArea     
   
for i in range(0, maximum):
    visited = [[False] * n for _ in range(n)]
    safeArea = 0
    for row in range(n):
        for col in range(n):
            value = dfs(row, col, i)
            if value:
                safeArea +=1 
    answer.append(safeArea)
    if answer[-1] > safeArea:
        break
print(max(answer))    