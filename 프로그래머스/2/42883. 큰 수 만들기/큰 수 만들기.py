def solution(number, k):
    answer = ''
    n_list = list(map(int, number))
    stack = []
    for number in n_list:
        if k >0:
            while stack and k >0:
                if stack[-1] >= number:
                    break
                stack.pop()
                k-=1
            stack.append(number)
                    
        else:
            stack.append(number)
    for _ in range(k):
        stack.pop()
    return ''.join(map(str, stack))