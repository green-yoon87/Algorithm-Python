import sys
input = sys.stdin.readline
def dfs(idx, depth):
    if depth == 6:
        print(*stack)
    for i in range(idx, num):
        stack.append(arr[i])
        dfs(i+1, depth+1)
        stack.pop()
    

while True:
    arr = list(map(int, input().split()))
    num = arr[0]
    arr = arr[1:]
    stack = []
    if num == 0:
        exit()
    dfs(0, 0)
    print()
    