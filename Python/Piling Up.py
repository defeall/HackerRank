T=int(input())
for i in range(T):
    n=int(input())
    a=list(map(int,input().split()))
    if([a[i]>a[i+1] or a[n-i-1]>a[n-i-2] for i in range((n//2)-1)]):
        print('Yes')
    else:
        print('No')
