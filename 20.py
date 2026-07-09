s = input()
chars = input().split()

indices = []
for i in range(len(s)-1, -1, -1):
    if s[i] in chars:
        indices.append((i, s[i]))

for idx, ch in indices:
    print(f"{idx} {ch}")

print(indices)