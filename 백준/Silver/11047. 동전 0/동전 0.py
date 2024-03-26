import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coin = int(input())
    coins.append(coin)
coins.reverse()
answer = 0
for coin in coins:
    answer += k // coin
    k = k % coin
    if k == 0:
        break
print(answer)  