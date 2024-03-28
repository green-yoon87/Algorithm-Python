from collections import deque
def solution(n, lost, reserve):
    students, clothes= [], []
    for student in lost:
        if student not in reserve:
            students.append(student)
    for clothe in reserve:
        if clothe not in lost:
            clothes.append(clothe)
    lost, reserve = students, clothes
    lost.sort()
    reserve.sort()
    left = []
    while lost and reserve:
        student = lost.pop()
        clothe = reserve.pop()
        if clothe > student +1:
            lost.append(student)
        elif clothe < student -1:
            reserve.append(clothe)
            left.append(student)
        
    return n - len(lost) - len(left)