t=int(input())
for i in range(t):
    c=input().split()
    a,b=c[0],c[1]
    try:
        d=int(a)//int(b)
        print(d)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
    
