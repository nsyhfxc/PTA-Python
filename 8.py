n = eval(input())
sum = 0
fenzi = 1
fenmu = 1
for i in range(n):
    sum += fenzi / fenmu
    fenmu += 2
print(f"sum = {sum:.6f}")