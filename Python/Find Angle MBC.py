import math
ab=int(input())
bc=int(input())
theta=math.degrees(math.atan(ab/bc))
d=str(theta)
if(int(d[(d.index('.'))+1])<5):
    n=math.floor(theta)
else:
    n=math.ceil(theta)
print(str(n)+u"\N{DEGREE SIGN}")
