import string
size=int(input())
a = string.ascii_lowercase
l=[]
for i in range(size):
    s = "-".join(a[i:size])
    l.append(s[::-1]+s[1:])
width=len(l[0])
for i in range(size-1,0,-1):
    print(l[i].center(width,'-'))
for i in range(size):
    print(l[i].center(width,"-"))
