cube = lambda x: x*x*x

def fibonacci(n):
    l=[0,1]
    if(n==0):
        return []
    if(n==1):
        return [0]
    for i in range(2,n):
        a=l[i-1]+l[i-2]
        l.append(a)
    return l

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
