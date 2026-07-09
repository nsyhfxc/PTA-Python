lst = set(map(int,input().split(',')))
lst = list(lst)
res = []
for i in range(1,11):
    if (i not in lst) and (i > 5):
        res.append(i)
print(*res)