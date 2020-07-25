N,l=int(input()),list(map(int,input().split()))
if([all([i>0 for i in l])][0] == True):
    if([any([(str(i)[::-1]==str(i)) for i in l])][0]==True):
        print('True')
    else:
        print('False')
else:
    print('False')
