import re
t=int(input())
for i in range(t):
    S=input()
    try:
        re.compile(S)
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid)
