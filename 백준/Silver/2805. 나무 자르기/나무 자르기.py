import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

def cutTree(trees, mid):
      length = 0
      for tree in trees:
        if (tree - mid) >0:
            length += (tree - mid)
      return length
  
def binarySearch(trees):
    start, end = 0, max(trees)-1
    mid = 0
    while end >= start:
        mid = (start +end) //2
        length = cutTree(trees, mid)
        if length >= m: # 필요한 양보다 더 많은 나무 길이를 잘랐을 때 
            start = mid  + 1
        else: # 필요한 양보다 더 적게 나무 길이를 잘랐을 때
            end = mid - 1
    return end

print(binarySearch(trees))
