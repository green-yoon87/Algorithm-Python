from collections import deque
def solution(name):
    answer = 0
    ordList = []
    nameList = list(name)
    n = len(name)
    for i in nameList:
        if (ord(i) - ord('A') ) <= ( ord('Z') - ord (i) ) :
            ordList.append(ord(i) - ord('A'))
        else:
            ordList.append(ord('Z') - ord (i) + 1)
    move = n -1 
    for idx in range(n):
        nextIdx = idx +1
        while nextIdx < n and name[nextIdx] == "A":
            nextIdx+=1
        move = min([move, 2 * idx + (n-nextIdx), idx + (n-nextIdx) *2])
    answer += move
    return answer + sum(ordList)