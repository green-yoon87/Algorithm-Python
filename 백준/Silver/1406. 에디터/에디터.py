import sys
a = list(sys.stdin.readline().strip())
b=[]
n = int(input())
 
while n>0:
  n = n-1
  cmd = sys.stdin.readline().strip()
  if(cmd[0] =="L"):
    if a: b.append(a.pop())
    else: continue
  elif(cmd[0]=="D"):
    if b: a.append(b.pop())
    else: continue
  elif(cmd[0]=="B"):
    if a: a.pop()
    else: continue
  elif(cmd[0]=="P"):
    a.append(cmd[2])
  
  
print(''.join(a+list(reversed(b))))