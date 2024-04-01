def solution(clothes):
    answer = 0
    clothesDict = {}
    category = []
    for i in range(len(clothes)):
        if clothesDict.get(clothes[i][1], 0) == 0:
            clothesDict[clothes[i][1]] = [clothes[i][0]]
            category.append(clothes[i][1])
        else:
            clothesDict[clothes[i][1]].append([clothes[i][0]])

    for i in range(len(category)):
        temp = len(clothesDict[category[i]])
        for j in range(i+1, len(category)):
            temp *= (len(clothesDict[category[j]]) + 1)
        answer += temp 
    return answer