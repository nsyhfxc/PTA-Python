s = int(input())
for i in range(pow(10,s - 1),pow(10,s)):
    n = i
    sum = 0
    j = 0
    while(n):
        temp = n % 10
        sum += pow(temp,s)
        n //= 10
    if sum==i:
        print(sum)
