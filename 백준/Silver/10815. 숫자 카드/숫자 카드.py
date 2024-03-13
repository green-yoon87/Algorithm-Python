import sys
input = sys.stdin.readline

cardNumber = int(input())
cards = list(map(int, input().split()))

targetNumber = int(input())
targets = list(map(int, input().split()))

dictionary = {target:0 for target in targets}
for i in cards:
    if dictionary.get(i, -1) == 0:
        dictionary[i] = 1
for i in targets:
    print(dictionary[i], end = " ")