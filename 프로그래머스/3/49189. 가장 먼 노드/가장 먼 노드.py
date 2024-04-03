from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    q = deque([(1, 0)])
    visited[1]=True
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    depth = 0
    while q:
        popNode = q.popleft()
        if depth < popNode[1]:
            answer = 1
            depth = popNode[1]
        elif depth == popNode[1]:
            answer+=1
        for i in graph[popNode[0]]:
            if not visited[i]:
                visited[i] =True
                q.append((i, popNode[1]+1))
    return answer