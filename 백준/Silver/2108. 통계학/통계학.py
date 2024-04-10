import sys
input = sys.stdin.readline

n = int(input())
numbers = []
numbers1 = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
previousValue = 4001 
count = 0
numbers.sort()
for i in range(len(numbers)):
    if numbers[i] != previousValue:
        if i != 0:
            numbers1.append((count, previousValue))
        previousValue = numbers[i]
        count =1
    else:
        count+=1
    if i == len(numbers) -1:
        numbers1.append((count, numbers[i]))    
    
numbers1.sort(reverse = True, key = lambda x: (x[0], -x[1]))
print(round(sum(numbers) / n))
print(numbers[n//2])
if len(numbers1)> 1 and numbers1[0][0] == numbers1[1][0]:
    print(numbers1[1][1])
else:
    print(numbers1[0][1])
    
print(numbers[-1] - numbers[0])