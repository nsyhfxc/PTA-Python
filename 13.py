lower, upper = map(int, input().split())
if lower > upper or upper > 100:
    print("Invalid.")
else:
    print("fahr celsius")
    for f in range(lower, upper + 1, 2):
        c = 5 * (f - 32) / 9
        print(f"{f}{c:6.1f}")
