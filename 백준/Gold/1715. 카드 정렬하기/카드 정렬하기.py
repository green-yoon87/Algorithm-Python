import sys
from queue import PriorityQueue

input = sys.stdin.readline
num = int(input())
cards = PriorityQueue(maxsize = num)
for i in range(num):
    card = int(input())
    cards.put(card)
answer = 0
while cards.qsize()>1:
    card1 = cards.get()
    card2 = cards.get()
    newCard = card1 + card2
    answer += newCard
    cards.put(newCard)

print(answer)
    
