import math
import os
import random
import re
import sys
import calendar
# Complete the time_delta function below.
def time_delta(t1, t2):
    x1 = t1.split(" ")
    x2 = t2.split(" ")
    b1,c1 = x1[4],x1[5]
    b2,c2 = x2[4],x2[5]
    m =['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    d1=[31,59,90,120,151,181,212,243,273,304,334,365,0]
    d2=[31,60,91,121,152,182,213,244,274,305,335,366,0]
    l1=(((int(x1[3])-1)//4)-((int(x1[3])-1)//100)+((int(x1[3])-1)//400))
    l2=(((int(x2[3])-1)//4)-((int(x2[3])-1)//100)+((int(x2[3])-1)//400))
    y1=((l1*366)+((int(x1[3])-1-l1)*365))*24*3600
    y2=((l2*366)+((int(x2[3])-1-l2)*365))*24*3600
    if(calendar.isleap(int(x1[3]))==True):
        m1=d2[m.index(x1[2])-1]
    else:
        m1=d1[m.index(x1[2])-1]
    if(calendar.isleap(int(x2[3]))==True):
        m2=d2[m.index(x2[2])-1]
    else:
        m2=d1[m.index(x2[2])-1]
    n1=(m1+int(x1[1])-1)*24*3600
    n2=(m2+int(x2[1])-1)*24*3600
    if(c1[0]=='-'):
        s1=((int(b1[:2])*3600)+(int(b1[3:5])*60)+int(b1[6:]))+((int(c1[1:3])*3600)+(int(c1[3:])*60))
    else:
        s1=((int(b1[:2])*3600)+(int(b1[3:5])*60)+int(b1[6:]))-((int(c1[1:3])*3600)+(int(c1[3:])*60))
    if(c2[0]=='-'):
        s2=((int(b2[:2])*3600)+(int(b2[3:5])*60)+int(b2[6:]))+((int(c2[1:3])*3600)+(int(c2[3:])*60))
    else:
        s2=((int(b2[:2])*3600)+(int(b2[3:5])*60)+int(b2[6:]))-((int(c2[1:3])*3600)+(int(c2[3:])*60))
    a1=y1+n1+s1
    a2=y2+n2+s2
    diff=abs(a1-a2)
    return str(diff)

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)


