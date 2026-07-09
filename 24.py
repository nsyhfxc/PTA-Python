n = int(input())
s = list(map(int,input().split()))
maxnum = s[0]
index = 0
for i in range(0,n):
    if(s[i] > maxnum):
        maxnum = s[i]
        index = i
print(f"{maxnum} {index}")