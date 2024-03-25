import sys
input = sys.stdin.readline

num = int(input())
n_list = list(map(int, input().split()))
n_list.sort(reverse = True)
answer = n_list[0] * (num-1) + sum(n_list[1:])
print(answer)