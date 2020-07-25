a=input()
k=int(input())
b=len(a)//k
for i in range(b):
    c=a[k*i:(k*i)+k]
    d=[]
    for j in range(k):
        if(c[j] in d):
            continue
        else:
            print(c[j],end='')
            d.append(c[j])
    print('\n',end='')
