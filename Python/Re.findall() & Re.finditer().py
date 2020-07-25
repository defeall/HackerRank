import re
txt = input()
y=(list(map(lambda x: x.group(),re.finditer(r'[aeiouAEIOU][aeiouAEIOU]+',txt))))
if(len(y)>0):
    for i in y:
        if(txt.index(i)==(len(txt)-len(i)) or txt.index(i)==0):
           continue
        print(i)
else:
    print('-1')
