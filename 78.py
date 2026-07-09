n = int(input())
if n <= 0:
    exit()
lst = [list(map(int, input().split())) for i in range(n)]
h = dict()
l = dict()
for i in range(n):
    max_h = max(lst[i][j] for j in range(n))
    min_l = min(lst[k][i] for k in range(n))
    h.update({(i, j): lst[i][j] for j in range(n) if lst[i][j] == max_h})  # 保存行最大值坐标
    l.update({(k, i): lst[k][i] for k in range(n) if lst[k][i] == min_l})  # 保存列最小值坐标
 
lst_ad = list(set(h) & set(l))
print(len(lst_ad))