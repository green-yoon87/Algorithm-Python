from collections import deque

def solution(priorities, location):
    answer = 0
    maximum = max(priorities)
    queue = deque([(i, idx) for idx, i in enumerate(priorities)])
    order = 0
    
    while queue:
        element = queue.popleft()
        if element[0] < maximum:
            queue.append(element)
        else:
            order +=1
            if element[1] == location: # 실행 순서를 알아야하는 프로세스 
                return order
            else:
                maximum = max(queue)[0]
    
        
    return order
