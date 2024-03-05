import sys
n, k = map(int, sys.stdin.readline().split())
circle, answer = [], []

def solution(n, k):
    for i in range(n):
        circle.append(i+1)
    index = 0
    while circle:
        index = (k - 1 + index) % len(circle)
        element = circle.pop(index)
        answer.append(element)
    print("<", end = "")
    for i in range(len(answer)):
        if i == len(answer)-1:
            print(answer[i], end= "")
        else:
            print(answer[i], ", ", sep="",  end= "")
    print(">")

solution(n, k)