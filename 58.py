n = int(input())
lst = list()
for i in range(n):
    lst.append(list(map(int, input().split())))
sums = 0
for i in range(n):
    for j in range(n):
        if i != (n - 1) and j != (n - 1) and i + j != (n - 1):
            sums += lst[i][j]
print(sums)