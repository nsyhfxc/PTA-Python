lst = eval(input().strip())
new = []
for item in lst:
    if item not in new:
        new.append(item)
print(*new)