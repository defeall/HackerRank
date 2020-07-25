import re
n=int(input())
for i in range(n):
    name,email=input().split()
    e=email[1:-1]
    if(bool(re.findall(r'^[A-Za-z][\w\.-]+[@]{1}[A-Za-z]+\.[a-zA-Z]{1,3}',e))==True):
        print(name,email)
