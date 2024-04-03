def solution(sizes):
    answer = 0
    width, height = [], []
    for i in sizes:
        width.append(i[0])
        height.append(i[1])
    answer = max(width) * max(height)
    for i in range(len(sizes)):
        temp = width[i]
        if width[i] > height[i]:
            width[i] = height[i]
            height[i] = temp
        answer = min(answer, max(width) * max(height))
        
    return answer