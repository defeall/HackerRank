from collections import namedtuple
n=int(input())
a=namedtuple('a',','.join(input().split()))
t=0
for i in range(n):
    l=list(map(str,input().split()))
    w,x,y,z=l[0],l[1],l[2],l[3]
    b=a(w,x,y,z)
    t=t+int(b.MARKS)
print('%.2f'%(t/n))
