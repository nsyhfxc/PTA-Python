error = float(input())
ans = 1.0
fa = 1
n = 1
term = 1.0
while abs(term) >= error:
  fa *= n
  term = 1.0 / fa
  ans += term
  n += 1
print(f"{ans:.6f}")