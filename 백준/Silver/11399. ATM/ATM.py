import sys
input = sys.stdin.readline

num = int(input())
takingTime = list(map(int, input().split()))
takingTime.sort()
sum = 0
for i in range(num):
    sum += takingTime[i] * (num -i)
print(sum)