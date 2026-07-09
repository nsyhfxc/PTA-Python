weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
check_map = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

n = int(input())
ids = [input().strip() for _ in range(n)]
invalid = []

for id in ids:
    if not id[:17].isdigit():
        invalid.append(id)
        continue
    total = sum(int(id[i]) * weights[i] for i in range(17))
    if check_map[total % 11] != id[17]:
        invalid.append(id)

if invalid:
    for i in invalid:
        print(i)
else:
    print("All passed")