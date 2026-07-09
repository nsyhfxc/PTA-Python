n = eval(input())
sum = 0
fenzi = 1
fenmu = 1
cnt = 1
for i in range(n):
    sum += cnt * (fenzi / fenmu)
    cnt = -cnt
    fenzi += 1
    fenmu += 2
print(f"{sum:.3f}")