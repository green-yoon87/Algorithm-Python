def solution(s):
    answer = True
    s = list(s)
    sum = 0
    for i in s:
        if i == "(":
            sum += 1
        elif i == ")":
            sum -= 1
        if(sum <0):
            return False
    if sum == 0:
        answer = True
    else:
        answer = False
    

    return answer