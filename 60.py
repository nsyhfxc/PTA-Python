T = int(input())
for i in range(T):
    n = int(input())
    lst = list()
    for j in range(n):
        lst.append(list(map(int, input().split())))
    flag = True
    for ii in range(n):
        for jj in range(ii):
            if lst[ii][jj] != 0:
                flag = False
                break
        if flag is False:
            break
    print("YES" if flag else "NO")