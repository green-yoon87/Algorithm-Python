answer = 0
def dfs(idx, target, numbers, num):
    global answer
    if idx == len(numbers):
        if num == target:
            answer +=1
        return
    dfs(idx+1, target, numbers, num+numbers[idx])
    dfs(idx+1, target, numbers, num-numbers[idx])

def solution(numbers, target):
    global answer 
       

    dfs(0, target, numbers, 0)
    return answer
    