def solution(prices):
    answers = []
    for i in range(len(prices)):
        answer = 0
        for j in range(i, len(prices)-1):
            if prices[i] <= prices[j]:
                answer +=1
            else:
                break
        answers.append(answer)      
    return answers
