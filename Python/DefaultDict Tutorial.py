from collections import defaultdict
a=input().split()
n,m=int(a[0]),int(a[1])
l1=defaultdict(list)
for i in range(n):
    b=input()
    l1[i].append(b)
l2=[]
for i in range(m):
    c=input()
    l2.append(c)
for i in range(m):
    d=0
    for j in range(n):
        if(l1[j][0]==l2[i]):
            d=d+1
            print(j+1,end=' ')
    if(d==0):
        print('-1')
    print('\n',end='')
