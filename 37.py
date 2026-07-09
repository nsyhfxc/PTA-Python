n = int(input())
res = []
while(n):
    res.append(n % 10)
    n //= 10
ans = ""
for ch in res:
    ans += str(ch)
print(int(ans))