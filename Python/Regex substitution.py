import re
n=int(input())
def rep(match):
    if(match.group(0)==' && '):
        return ' and '
    elif(match.group(0)==' || '):
        return ' or '
    elif(match.group(0)==' &| ' or match.group(0)==' |& '):
        return match.group(0)
for i in range(n):
    s=input()
    print(re.sub(r'\s[&|]{2}\s',rep,s))


#####2222nndd mmethod######
    import re
n = int(input())
list1 = []
for i in range(n):
    s = input()

    s = re.sub(r'(?<= )&&(?= )','and',s)
    
    s = re.sub('(?<= )\|\|(?= )','or',s)
    print(s)   
