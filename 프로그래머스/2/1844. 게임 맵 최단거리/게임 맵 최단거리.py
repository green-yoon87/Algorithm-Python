from collections import deque
answer = 0
def solution(maps):
    global answer
    
    bfs(0, 0, maps)
    return answer

def bfs(row, col, maps):
    global answer
    
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q = deque([(row, col, 1)])
    visited[row][col] = True
    answer = -1
    while q:
        popNode = q.popleft()
        row1, col1, depth1 = popNode[0], popNode[1], popNode[2]
        if row1 == n-1 and col1 == m-1:
            answer = depth1
            break
        if row1>0 and maps[row1-1][col1] == 1 and not visited[row1-1][col1]:
            q.append((row1-1, col1, depth1 +1))
            visited[row1-1][col1] = True
        if col1>0 and maps[row1][col1-1] == 1 and not visited[row1][col1-1]:
            q.append((row1, col1-1, depth1 +1))
            visited[row1][col1 -1] = True
        if row1<n-1 and maps[row1+1][col1] == 1 and not visited[row1+1][col1]:
            q.append((row1+1, col1, depth1 +1))
            visited[row1 +1][col1] = True
        if col1<m-1 and maps[row1][col1+1] == 1 and not visited[row1][col1+1]:
            q.append((row1, col1+1, depth1 +1))
            visited[row1][col1 +1] = True
            