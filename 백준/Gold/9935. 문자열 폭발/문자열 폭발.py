import sys
input = sys.stdin.readline

str = input().strip()
explodedStr = input().strip()
answer = []
for i in str:
    if i != explodedStr[-1]:
        answer.append(i)
    else:
        if len(answer)>= len(explodedStr)-1:
            word = i
            for j in range(len(explodedStr)-1):
                word += answer.pop()
            if word[::-1] != explodedStr:
                for k in word[::-1]:
                    answer.append(k)
        else:
            answer.append(i)
if answer:
    print("".join(answer))
else:
    print("FRULA")