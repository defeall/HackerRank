n,a,k=int(input()),''.join(input().split()),int(input())
from itertools import combinations
b=list(combinations(a,k))
s=0
for j in range(len(b)):
    if('a' in b[j]):
        s=s+1
print('%.3f'%(s/len(b)))
