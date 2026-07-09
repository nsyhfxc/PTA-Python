m,n = map(int,input().split())
lst = []
for i in range(m):
    lst.append(list(map(int,input().split())))
for i in range(m):
    s = 0
    for j in range(n):
        s += lst[i][j]
    print(s)