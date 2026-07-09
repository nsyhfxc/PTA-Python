n = int(input())
if n != 0:
    slist = list(map(int,input().split()))
    sum = 0
    for i in range(n):
        sum += slist[i]
    aver = sum / n
    cnt = 0
    for i in range(n):
        if slist[i] >= 60:
            cnt += 1
    print(f"average = {aver:.1f}")
    print(f"count = {cnt}")
else:
    print('average = 0.0\ncount = 0')