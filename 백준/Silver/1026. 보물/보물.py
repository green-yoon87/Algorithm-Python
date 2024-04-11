import sys
input = sys.stdin.readline
n = int(input())
firstList = list(map(int, input().split()))
secondList = list(map(int, input().split()))

firstList.sort()
secondList.sort(reverse = True)
answer = 0
for i in range(n):
    answer += firstList[i] * secondList[i]
print(answer)