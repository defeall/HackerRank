a=input().split()
N,X=int(a[0]),int(a[1])
l=[]
for i in range(X):
    l1=list(map(float,input().split()))
    l.append(l1)
l2=list(zip(*l))
for i in range(N):
    print('%.1f'%((sum(l2[i]))/X))
