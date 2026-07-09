s = input()
ans = []
for i in s:
    if(i.isdigit()):
        ans.append(i)
res = "".join(ans)
print(int(res))