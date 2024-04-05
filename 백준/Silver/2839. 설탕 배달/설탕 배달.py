import sys
input = sys.stdin.readline
n = int(input())
answer = 0
if n % 5 == 0:
    answer = n // 5
    n = 0
elif n % 3 == 0:
    if n > 15:
        answer = (n //15 ) * 3
        n = n % 15
    answer += n // 3
    n = 0
else:
    while True:
        if n -5 <0:
            break
        if n % 3 == 0:
            if n > 15:
                answer += (n //15 ) * 3
                n = n % 15
            break   
        n -= 5
        answer +=1
    answer += n // 3
    n = n % 3

if n > 0:
    answer = -1
print(answer)