n,a = int(input()),'A'
for I in range(n):
    for i in range(n - I):
        print(a,'',end = '')
        a = chr(ord(a) + 1)
    print()