n = int(input())
cnt = 0
sum = 0
while(n):
    sum += (n % 10)
    cnt += 1
    n //= 10
print(f"{cnt} {sum}")