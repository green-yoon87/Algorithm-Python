def solution(progresses, speeds):
    answer = []
    takeDays = []
    
    for i in range(len(progresses)):
        progress, speed = progresses[i], speeds[i]
        days = 0
        while True:
            progress += speed
            days +=1
            if progress >=100:
                break
        takeDays.append(days)
        
    i = 0
    function = 1
    firstDay = 0
    takeDays.reverse()
    if len(takeDays) == 1:
        answer.append(function)
    firstDay = takeDays.pop()
    
    while takeDays:  
        day = takeDays.pop()
        if firstDay >= day:
            function +=1
        else:
            firstDay = day
            answer.append(function)
            function = 1
            
        if len(takeDays) == 0:
            answer.append(function)
            
    return answer

# progresses: 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열
# speeds: 각 작업의 개발 속도가 적힌 정수 배열 
# solution: 각 배포 마다 몇 개의 기능이 배포되는지 return 