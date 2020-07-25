from itertools import product
A, B = input().split(" ")
list2 = []
for i in range(int(A)):
    list1 = list(map(int, input().split()))
    list1 = list1[1:]
    list2.append(list1)

CrossProduct = list(product(*list2))

ans = [((sum(i**2 for i in n))%int(B)) for n in CrossProduct]

print(max(ans))
