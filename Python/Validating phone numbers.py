import re
N=int(input())
for i in range(N):
    p=input()
    if(bool(re.match(r'^[7-9][0-9]{9}$',p))==True):
        print('YES')
    else:
        print('NO')
