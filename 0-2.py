from math import sqrt
def PrimeSum(m,n):
    sum = 0
    for i in range(m,n+1):
        if(prime(i)):
            sum += i
    return sum
def prime(p):
    if(p < 2):
        return False
    else:
        for i in range(2,int(sqrt(p)) + 1):
            if(p % i == 0):
                return False
    return True

m, n = input().split()
m = int(m)
n = int(n)
print(PrimeSum(m, n))