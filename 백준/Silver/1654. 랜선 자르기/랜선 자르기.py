import sys  
input = sys.stdin.readline

k, n = map(int, input().split())
lines = []

for i in range(k):
    line = int(input())
    lines.append(line)
lines.sort()
def binarySearch(lines):
    maximum = max(lines)
    start, end, mid= 1, int(sum(lines) /n), 0
    while end != mid:
        mid = int((start+ end) /2)
        num = 0
        for line in lines:
            num += int(line / mid)
        if num >= n: 
            start = mid + 1
        else:
            if mid != 1:
                end = mid - 1
            else:
              return end

    return mid
print(binarySearch(lines))  