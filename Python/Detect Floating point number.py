b=int(input())
for i in range(b):
    a=input()
    try:
        if(float(a)):
            if((a[0]=='+' or a[0]=='-' or a[0]=='.' or int(a[0])) and (a.count('.')==1) and(a[-1]!='.') ):
                print('True')
            else:
                print('False')
    except ValueError as f:
        print("False")
    
