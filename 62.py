m, n = map(int, input().split())
lst = list()
for i in range(m):
    lst.append(list(map(int, input().split())))
flag = True
for i in range(m):
    for j in range(n):
        if i != 0 and i != (m - 1) and j != 0 and j != (n - 1) and \
        lst[i][j] > lst[i - 1][j] and lst[i][j] > lst[i + 1][j] and \
        lst[i][j] > lst[i][j - 1] and lst[i][j] > lst[i][j + 1]:
            print(f"{lst[i][j]} {i + 1} {j + 1}")
            flag = False
if flag:
    print(f"None {i + 1} {j + 1}")