import sys

num = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))
towers = [(height, idx) for idx, height in enumerate(towers)]
answer = [0 for _ in range(num)]
stack = []

for i in range(num-1, -1, -1):
    tower = towers.pop()
    while stack:
        if tower[0] >= stack[-1][0]: 
            element = stack.pop()
            answer[element[1]] = tower[1] + 1
        else:
          break

    stack.append(tower)         
for i in answer:
    print(i, end=" ")