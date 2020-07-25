n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(N):
    o=input().split()
    if(o[0]=='pop'):
        s.pop()
    elif(o[0]=='remove'):
        x=int(o[1])
        s.remove(x)
    elif(o[0]=='discard'):
        x=int(o[1])
        s.discard(x)
print(sum(s))
