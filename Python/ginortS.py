import re
S=input()
A,B,C,D=re.findall(r'[a-z]',S),re.findall(r'[A-Z]',S),re.findall(r'[13579]',S),re.findall(r'[02468]',S)
A.sort(),B.sort(),C.sort(),D.sort()
print(*A,sep='',end='')
print(*B,sep='',end='')
print(*C,sep='',end='')
print(*D,sep='',end='')
