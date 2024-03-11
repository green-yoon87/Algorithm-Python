def solution(n, times):
    start, end = 1, min(times) * n
    while start <= end:
        mid = (start + end) // 2
        num = 0
        for time in times:
            num+= mid //time
        if num < n:
            start = mid +1
        else:
            end = mid -1        
    return start

