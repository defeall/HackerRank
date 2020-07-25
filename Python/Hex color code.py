import re
n=int(input())
for i in range(n):
    s=input()
    if(len(s)!=4 ):
       if(bool(re.findall(r'[ :][#][a-fA-F0-9]{3,6}',s))==True):
           l1=(re.findall(r'[#][a-fA-F0-9]{3,6}',s))
           for i in l1:
               print(i)
