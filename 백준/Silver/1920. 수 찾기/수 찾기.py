import sys
input = sys.stdin.readline

n = int(input())
numArr = list(map(int, input().split()))

m = int(input())
findArr = list(map(int, input().split()))
dictionary = {num:0 for num in findArr}

for i in numArr:
    if dictionary.get(i, -1) == 0:
        dictionary[i] = 1

for i in findArr:
    print(dictionary[i])