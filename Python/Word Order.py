n=int(input())
l1,b={},0
for i in range(n):
    a=input()
    if(a not in l1):
        l1[a]=1
    else:
        l1[a]=l1[a]+1
print(len(l1.keys()))
for i in l1:
    print(l1[i],end=' ')
