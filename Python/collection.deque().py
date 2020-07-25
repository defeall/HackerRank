from collections import deque
N=int(input())
d=deque()
for i in range(N):
    o=input().split()
    if(o[0]=='append'):
        a=int(o[1])
        d.append(a)
    elif(o[0]=='appendleft'):
        a=int(o[1])
        d.appendleft(a)
    elif(o[0]=='pop'):
        d.pop()
    elif(o[0]=='popleft'):
        d.popleft()
for i in d:
    print(i,end=' ')
