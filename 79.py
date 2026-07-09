nums = list(map(int, input().split(',')))
target = int(input())
found = False
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)
            found = True
            break
    if found:
        break

if not found:
    print("no answer")