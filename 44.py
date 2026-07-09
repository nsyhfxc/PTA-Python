n = int(input())
e = 1.0
term = 1.0
for i in range(n):
    e += 1/(term)
    term = term * (i + 2)
print(f"{e:.8f}")
