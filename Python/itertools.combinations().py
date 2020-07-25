from itertools import combinations
a=input().split()
S,k=a[0],int(a[1])
S=''.join(sorted(S))
for i in range(k):
    b=list(combinations(S,i+1))
    for j in range(len(b)):
       print(''.join(b[j]))
