import sys
input = sys.stdin.readline
zero = [1, 0, 1]
one = [0, 1, 1]
def solution(n):
    global zero
    global one
    length = len(zero)
    if length <= n:
        for i in range(length, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[n], one[n])
    
num = int(input())
for _ in range(num):
    solution(int(input()))