m, n = map(int, input().split())
total = 0
for i in range(m, n + 1):
    total += i ** 2 + 1 / i
print(f"sum = {total:.6f}")