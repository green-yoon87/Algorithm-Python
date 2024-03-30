import sys
from collections import deque
input =sys.stdin.readline
tomatoes = []
q = deque([])
m, n = map(int, input().split())
for i in range(n):
    n_list = list(map(int, input().split()))
    tomatoes.append(n_list)
    for j in range(m):
        if n_list[j] == 1:
            q.append((i, j, 0)) 
def bfs():
    answer = 0
    while q:
        popTomato = q.popleft()
        row, col, depth = popTomato[0], popTomato[1], popTomato[2]
        if row > 0 and tomatoes[row-1][col] == 0:
            q.append((row-1, col, depth+1))
            tomatoes[row-1][col] = 1
            
        if col >0 and tomatoes[row][col-1] == 0:
            q.append((row, col-1, depth+1))
            tomatoes[row][col-1] = 1
        if row < n-1 and tomatoes[row+1][col] == 0:
            q.append((row+1, col, depth+1))
            tomatoes[row+1][col] = 1
        if col < m-1 and tomatoes[row][col+1] == 0:
            q.append((row, col+1, depth +1))
            tomatoes[row][col+1] = 1
        if not q:
            answer = depth
    return answer
value = bfs()
if any (0 in line for line in tomatoes):
    print(-1)
else:
    print(value)