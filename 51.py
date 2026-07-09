n = int(input())
a,b = 1,1
arr = []
for i in range(100):
    arr.append(a)
    a,b = b,a + b
for i in range(100):
    if(n < arr[i]):
        print(f"{arr[i]}")
        break