import re
n = int(input())
for i in range(n):
    s=input()
    if re.search(r'[a-zA-Z0-9]{10}',s):
        if not re.search(r'.*(.).*\1',s):
            if re.search(r'[a-zA-Z0-9]*[A-Z][a-z0-9]*[A-Z][a-zA-Z0-9]*',s):
                if re.search(r'[a-zA-Z0-9]*[0-9][a-zA-Z]*[0-9][a-zA-Z]*[0-9][a-zA-Z0-9]*',s):
                    print('Valid')
                else:
                    print('Invalid')
            else:
                print('Invalid')
        else:
            print('Invalid')
    else:
        print('Invalid')
