import sys
input = sys.stdin.readline

a, p = map(int, input().split())
check = [0 for _ in range(4 * (9**5) +1)]

def calculate(a, p):
    n_list = list(map(int, str(a)))
    num = 0
    for i in n_list:
        num += i ** p
    return num

def dfs(a, p, check, depth):
    if check[a] != 0:
        return check[a] -1
    depth +=1
    check[a] = depth 
    a = calculate(a, p)   
    return dfs(a, p, check, depth)   

depth = 0
print(dfs(a, p, check, depth))