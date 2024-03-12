import sys
input = sys.stdin.readline

cardNum = int(input())
cards = list(map(int, input().split()))

targetCardNum = int(input())
cardsToFind = list(map(int, input().split()))
dictionary = {card : 0 for card in cardsToFind}

for card in cards:
    if dictionary.get(card, -1) != -1:
        dictionary[card] +=1
for card in cardsToFind:
    print(dictionary[card], end = " ")
