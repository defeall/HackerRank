A=list(map(int,input().split()))
n=int(input())
y=0
for i in range(n):
    B=list(map(int,input().split()))
    x=0
    for j in range(len(B)):
        if(B[j] in A):
            continue
        else:
            x=x+1
            break
    if(x==0 and len(A)==len(B) or x>0):
        y=0
        break
    else:
        y=y+1
if(y>0):
    print('True')
else:
    print('False')
