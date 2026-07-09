def gcd(m,n):
    if(not n):
        return m
    else:
        return gcd(n,m%n)
def lcd(m,n):
    return m / gcd(m,n) * n
m,n = map(eval,input().split())
print(f"{int(gcd(m,n))} {int(lcd(m,n))}")