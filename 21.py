ch = input()
s = input()

index = -1

for i in range(len(s)):
    if s[i] == ch:
        index = i

if index != -1:
    print(f"index = {index}")
else:
    print("Not Found")