import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
num = min(n//2, m)
answer = 0
for i in range(num, 0, -1):
    if n//2 >= i and m >= i and (n - 2* i + m - i) >= k:
        answer = i
        break
print(answer)  