T=int(input())
for i in range(T):
    n=int(input())
    A=list(map(int,input().split()))
    m=int(input())
    B=list(map(int,input().split()))
    x=0
    for j in range(n):
        if(A[j] in B):
            continue
        else:
            x=x+1
            break
    if(x>0):
        print('False')
    else:
        print('True')
