n = int(input())
sum = 0
fenzi = 2
pre_fenzi = 0
fenmu = 1
for i in range(n):
    sum += fenzi / fenmu
    pre_fenzi = fenzi
    fenzi += fenmu
    fenmu = pre_fenzi
print(f"{sum:.2f}")