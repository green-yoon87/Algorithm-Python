answer = 0
def solution(k, dungeons):
    global answer
    dungeons.sort(reverse = True, key = lambda x: (x[0], -x[1]))
    def dfs(node, k, num, visited):
        global answer
        num +=1
        visited.append(node)
        answer = max(answer, num)
        k -= dungeons[node][1]
        for i in range(len(dungeons)):
            if i not in visited and k >= dungeons[i][0]:
                dfs(i, k, num, visited[:])
                
    for i in range(len(dungeons)):
        dfs(i, k, 0, [])
        
    return answer