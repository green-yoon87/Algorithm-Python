import sys
input = sys.stdin.readline
num_list = list(map(int, str(input().strip())))
num_list.sort(reverse = True)
if num_list[-1] != 0 or sum(num_list) % 3 != 0:
    print(-1)
else:
    print(''.join(map(str, num_list)))