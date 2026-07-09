s = input()
res = set("".join(s))
ans = []
for i in res:
    ans += i
ans.sort()
for i in ans:
    print(i,end="")