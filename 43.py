def prime(n):
    if(n < 2):
        return False
    for i in range(2,int(n ** 0.5) + 1,1):
        if n % i == 0:
            return False
    return True
n = int(input())
for i in range(n):
    if(prime(i) and prime(n - i)):
        print(f"{n} = {i} + {n - i}")
        break

