def solution(s, skip, index):
    alpha =""
    answer =''
    for i in range(26):
        alpha += chr(ord('a') + i)
        
    for i in list(skip):
        alpha= alpha.replace(i, "")

    
    for str in s: 
        location = (alpha.find(str) + index) % len(alpha)
        answer += alpha[location]
    return answer

