def solution(answers):
    answer = []
    sheet1 = [1, 2, 3, 4, 5 ] * (len(answers) // 5 + 1)
    sheet2 = [2,1,2,3, 2,4, 2, 5] * (len(answers) //8 +1)
    sheet3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers) // 10 +1)
    value = [0, 0 , 0]
    for i in range(len(answers)):
        if sheet1[i] == answers[i]:
            value[0] +=1
        if sheet2[i] == answers[i]:
            value[1] +=1
        if sheet3[i] == answers[i]:
            value[2] +=1
    maximum = max(value)
    for i in range(len(value)):
        if value[i] == maximum:
            answer.append(i+1)
    return answer