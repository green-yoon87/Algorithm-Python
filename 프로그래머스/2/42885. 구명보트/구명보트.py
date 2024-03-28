def solution(people, limit):
    answer = 0
    people.sort()
    start, end = 0, len(people) -1
    while True:
        if start == end:
            answer += 1 
            break
        if start > end:
            break
        if people[start] + people[end] <= limit:
            answer += 1
            start +=1
            end -=1
        else:
            end -=1
            answer +=1
        
    return answer