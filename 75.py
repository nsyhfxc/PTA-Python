n = int(input())
m = list(map(int, input().split()))
dic = dict()
for i in m[:n]:
    dic[i] = dic.get(i, 0) + 1
for i in sorted(dic):
    print(f"{i}:{dic[i]}")