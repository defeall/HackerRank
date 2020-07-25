from collections import Counter
K=int(input())
n=list(map(int,input().split()))
l1,l2=list(Counter(n).keys()),list(Counter(n).values())
for i in range(len(l2)):
    if(l2[i]==1):
        r=l1[i]
        break
print(r)
               
