height = list(map(int,input().split()))
totalnum = len(height)
aver = sum(height) / totalnum
for i in height:
    if(i > aver):
        print(f"{i}",end=" ")