n = int(input())
num = 0
tot = 0
for i in range(n):
    dic = eval(input())
    for j in dic:
        t = dic[j]
        for k in t:
            num += 1
            tot += t[k]
print(f"{n:d} {num:d} {tot:d}")
