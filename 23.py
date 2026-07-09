a = list(map(int, input().split()))
n = a[0]
b = a[1:]
d = {}
for x in b:
    d[x] = d.get(x, 0) + 1

m = max(d.values())
for k in d:
    if d[k] == m:
        print(k, m)
        break