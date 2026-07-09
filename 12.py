nums = list(map(int, input().split()))
nums.sort(reverse=False)
print(f"{nums[0]}->{nums[1]}->{nums[2]}")