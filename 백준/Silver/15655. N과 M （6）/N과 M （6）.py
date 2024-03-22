import sys
input = sys.stdin.readline

n,m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
seq = []
def dfs(idx, depth):
    if depth == m:
        print(*seq)
        return
    for i in range(idx, n):
        seq.append(n_list[i])
        dfs(i+1, depth+1)
        seq.pop()
dfs(0, 0)