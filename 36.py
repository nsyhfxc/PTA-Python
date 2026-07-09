N = int(input())
t = []
for i in range(N):
    t.append(input())
maxl = 0
maxs = ''
for i in range(N):
    if len(t[i])>maxl:
        maxl = len(t[i])
        maxs = t[i]
print("The longest is:",maxs)
