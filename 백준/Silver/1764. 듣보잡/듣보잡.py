import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dict = {}
answer = []
for _ in range(n):
    name = input().strip()
    dict[name] = 1
for _ in range(m):
    name = input().strip()
    if dict.get(name, 0 ) == 1:
        answer.append(name)
print(len(answer))
answer.sort()
for i in answer:
    print(i)
    