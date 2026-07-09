def fn(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return fn(n - 1) * n
n = int(input())
sum = 0
a = 1
while(a <= n):
    sum += fn(a)
    a += 2
print(f"n={n},s={sum}")