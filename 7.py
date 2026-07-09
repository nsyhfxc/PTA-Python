a,n = map(int,input().split())
s = 0
term = a
for i in range(n):
    s += term
    term = term * 10 + a
print(f"s = {s}")