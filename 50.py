from math import sqrt
def prime(n):
    if(n < 2):
        return False
    for i in range(2,int(sqrt(n)) + 1,1):
        if(n % i == 0):
            return False
    return True
n = int(input())
arr = []
for i in range(n):
    arr.append(input())
for i in arr:
    if(prime(int(i))):
        print("Yes")
    else:
        print("No")