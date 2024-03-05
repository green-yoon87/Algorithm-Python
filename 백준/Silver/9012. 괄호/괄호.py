import sys
n = int(sys.stdin.readline())
while n>0:
  cmd = sys.stdin.readline()
  result =0
  for i in range(len(cmd)):
    if cmd[i]=='(':
      result= result+1
    elif cmd[i]==')':
      result =result-1
    if result<0:
      break
  if(result==0):
    print("YES")
  else: 
    print("NO")
  n=n-1