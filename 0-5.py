def f(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * f(n - 1)

def funcos(eps, x):
    sum = 0.0
    term = 1.0 
    i = 0
    while abs(term) > eps:
        sum += term
        i += 2
        term *= -x * x / (i * (i - 1))  # 递推公式
    return sum

eps, x = input().split()
eps, x = float(eps), float(x)
value = funcos(eps, x)
print("cos({0}) = {1:.4f}".format(x, value))
