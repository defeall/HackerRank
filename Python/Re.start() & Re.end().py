import re
S,K=input(),input()
b=0
for i in range(4):
    m=re.search(K,S)
    if m:
        a=(m.start()+b,m.end()+b-1)
        print(a)
        S=S[m.start()+1:]
        b=b+m.start()+1
    else:
        if(i==0):
            print('(-1, -1)')
        break
