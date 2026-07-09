a,b = map(int,input().split())
sum = 0
cnt = 0
for i in range(a,b + 1):
    sum += i
    print(f"{i:5d}",end="")
    cnt += 1
    if(cnt == 5):
        print("\n",end="")
        cnt = 0
if(cnt != 0):
    print()
print(f"Sum = {sum}",end="")