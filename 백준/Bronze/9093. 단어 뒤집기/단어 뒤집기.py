import sys

input = sys.stdin.readline
num = int(input())

for i in range(num):
    str = input().split()
    for i in str:
        a = list(i)
        a.reverse()
        print(''.join(a), end=" ")