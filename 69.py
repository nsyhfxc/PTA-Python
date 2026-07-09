from math import sqrt
m,n = map(int,input().split())
cnt = 0
for i in range(m,n + 1):
    lst=[1]
    for j in range(2,int(sqrt(i) + 1)):
        if i % j == 0:
            lst.append(j)
            if j * j != i:
                lst.append(i//j)
    lst.sort()
    if i == sum(lst):
        cnt += 1
        print(f"{i} = ",end="")
        print(" + ".join(str(lst[i]) for i in range(len(lst))))
if cnt == 0:
    print("None")