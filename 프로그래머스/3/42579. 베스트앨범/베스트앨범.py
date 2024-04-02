def solution(genres, plays):
    answer = []
    musicDict = {}
    generDict = {}
    for i in range(len(genres)):
        if musicDict.get(genres[i], 0) == 0:
            musicDict[genres[i]] = [(plays[i], i)]
        else:
            musicDict[genres[i]].append((plays[i], i))
        if generDict.get(genres[i], 0) == 0:
            generDict[genres[i]] = plays[i]
        else:
            generDict[genres[i]] += plays[i]
    genreList = []
    for i in set(genres):
        genreList.append((generDict[i], i))
    genreList.sort(reverse = True, key = lambda x: x[0])
    for i in genreList:
        temp = musicDict[i[1]]
        temp.sort(reverse = True, key = lambda x: (x[0], -x[1]))
        for j in temp[: min(2, len(temp))]:
            answer.append(j[1])   
    return answer