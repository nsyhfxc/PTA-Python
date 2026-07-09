from math import sqrt
def prime(n):
    if(n < 2):
        return False
    for i in range(2,int(sqrt(n)) + 1,1):
        if(n % i == 0):
            return False
    return True
m,n = map(int,input().split())
sum = 0
cnt = 0
for i in range(m,n + 1):
    if(prime(i)):
        sum += i
        cnt += 1
print(f"{cnt} {sum}")