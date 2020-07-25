from collections import OrderedDict
n=int(input())
od=OrderedDict()
l=[]
for i in range(n):
    a=input().split()
    name=' '.join(a[0:-1])
    price=int(a[-1])
    if name in l:
        od[name]=od[name]+price
    else:
        l.append(name)
        od[name]=price
for i in od:
    print(i,od[i])
