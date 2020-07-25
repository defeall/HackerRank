a=list(input())
a.sort()
l1,l2,b=[],[],0
for i in range(len(a)):
    if(a[i] not in l1):
        l1.append(a[i])
        l2.append(1)
    else:
        l2[l1.index(a[i])]=l2[l1.index(a[i])]+1
for i in range(3):
    m=l1[l2.index(max(l2))]
    print(m,max(l2))
    l1.remove(m)
    l2.remove(max(l2))
    
