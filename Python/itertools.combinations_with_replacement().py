from itertools import combinations_with_replacement
a=input().split()
S,k=a[0],int(a[1])
S=''.join(sorted(S))
b=list(combinations_with_replacement(S,k))
for i in range(len(b)):
   print(''.join(b[i]))
