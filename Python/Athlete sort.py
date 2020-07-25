import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    l=[]
    for i in range(n):
        l.append(arr[i][k])
    l.sort()
    for i in range(n):
        for j in range(n):
            if(arr[j][k]==l[i]):
                print(*arr[j],sep=' ')
                arr.remove(arr[j])
                break
