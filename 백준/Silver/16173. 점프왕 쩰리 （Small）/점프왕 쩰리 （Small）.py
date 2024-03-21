import sys
input = sys.stdin.readline

num = int(input())
matrix = []
visited = [[False] * num for _ in range(num)]
for _ in range(num):
    n_list = list(map(int, input().split()))
    matrix.append(n_list)
answer = "Hing"

def dfs(row, col):
    global answer
    count = matrix[row][col]
    visited[row][col] = True
    if count == -1:
        answer = "HaruHaru"
        return 
    if row + count < num and not visited[row+count][col]:
        dfs(row+count, col)
    if col + count < num and not visited[row][col + count]:
        dfs(row, col + count)
dfs(0, 0)
print(answer)