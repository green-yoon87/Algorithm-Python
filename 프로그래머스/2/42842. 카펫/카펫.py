def solution(brown, yellow):
    answer = []
    carpets = brown + yellow 
    height, width = 3, 0
    while True:
        width = carpets // height
        if height * width != carpets or (width -2 ) * (height -2) != yellow:
            height +=1
        else:
            answer.append(width)
            answer.append(height)
            break
    return answer