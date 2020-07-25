from collections import Counter
n1=int(input())
l1=list(map(int,input().split()))
n2=int(input())
m=0
l2,l3=list(Counter(l1).keys()),list(Counter(l1).values())
for i in range(n2):
    a=input().split()
    b,c=int(a[0]),int(a[1])
    if(b in l2):
        d=l2.index(b)
        if(l3[d]==0):
            continue
        else:
            m=m+c
            l3[d]=l3[d]-1
print(m)
