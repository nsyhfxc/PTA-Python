lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst1 = lst1[1:]
lst2 = lst2[1:]
ans = []
for i in lst1:
    if i not in lst2 and i not in ans:
        ans.append(i)
for i in lst2:
    if i not in lst1 and i not in ans:
        ans.append(i)
for i, num in enumerate(ans):
    if i != len(ans)-1:
        print("{} ".format(num), end="")
    else:
        print("{}".format(num))