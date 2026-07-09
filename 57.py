def find_king(n):
    king = 0
    for i in range(2, n + 1):
        king = (king + 3) % i
    return king + 1


n = int(input())
result = find_king(n)
print(f"{result}")
