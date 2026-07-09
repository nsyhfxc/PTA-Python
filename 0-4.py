def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def PrintFN(m, n):
    flist = []
    a, b = 1, 1
    idx = 0
    while a <= n:
        if a >= m:
            flist.append(a)
        a, b = b, a + b
        idx += 1
    return flist

m, n, i = input().split()
n = int(n)
m = int(m)
i = int(i)
b = fib(i)
print("fib({}) = {}".format(i, b))
fiblist = PrintFN(m, n)
print(len(fiblist))