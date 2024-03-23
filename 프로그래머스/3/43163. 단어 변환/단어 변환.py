from collections import deque
def solution(begin, target, words):
    answer = 0
    graph = [[] for _ in range(len(words) +1)] 
    index, visited = {}, {}
    words.append(begin)
    length = len(words[0])
    for i in range(len(words)):
        index[words[i]] = i


    for i in range(len(words)):
        word = list(words[i])
        for j in range(0, len(words)):
            word1 = list(words[j])
            oneWordDifferent = length 
            for k in range(length):
                if word[k] != word1[k]:
                    oneWordDifferent -=1
            if oneWordDifferent == length -1:
                graph[i].append(words[j])
    print(graph)
    q = deque([(begin, 0)])
    visited[begin] = True
    while q:
        popNode = q.popleft()
        print(popNode)
        word, depth = popNode[0], popNode[1]
        if word == target:
            answer = depth 
            break
        for c in graph[index[word]]:
            print(graph[index[word]])
            if not visited.get(c, False):
                q.append((c, depth+1))
                visited[c] = True     
    return answer