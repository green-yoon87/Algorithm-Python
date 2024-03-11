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
    start, end = 0, max(trees)
    mid = 0
    while end != mid:
        mid = int((start +end) /2)
        length = cutTree(trees, mid)
        if length > m: # 필요한 양보다 더 많은 나무 길이를 잘랐을 때 
            if cutTree(trees, mid+1) >= m:
                start = mid  + 1
            else:
                break
        elif length <m: # 필요한 양보다 더 적게 나무 길이를 잘랐을 때
            end = mid - 1
        else:
          break
    return mid

print(binarySearch(trees))