def solution(phone_book):
    answer = True
    phoneDict = {}
    phone_book.sort(key = lambda x: len(x))
    short, long = len(phone_book[0]), len(phone_book[1])
    for phone in phone_book:
        if len(phone) == short:
            phoneDict[phone] = 1
        else:
            for i in range(short, len(phone)):
                if phoneDict.get(phone[:i], 0) == 1:
                    answer = False
                    break
            phoneDict[phone] = 1
    
    return answer