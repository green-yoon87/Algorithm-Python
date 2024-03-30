import sys
input = sys.stdin.readline
n, m = map(int, input().split())
depth = 0
out = []
def dfs(start):
    if len(out) == m:
        print(* out)
        return 
    for i in range(start, n+1):
        out.append(i)
        dfs(i+1)
        out.pop()
dfs(1)
        
    