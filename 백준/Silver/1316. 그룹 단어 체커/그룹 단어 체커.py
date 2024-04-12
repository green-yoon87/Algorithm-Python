import sys
input = sys.stdin.readline
n = int(input())
answer = 0
for _ in range(n):
    dict = {}
    word = list(input().strip())
    previous = ""
    isGroupWord = True
    for i in word:
        if previous != i:
            if dict.get(i, 0) != 0:
                isGroupWord = False
                break
            else:
                dict[i] =1
                previous = i
    if isGroupWord:
        answer +=1
print(answer)   