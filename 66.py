N = input().split()
N = [int(i) for i in N]
a = max([N[0],N[1],N[2]])
b = max([N[3],N[4],N[5]])
c = max([N[6],N[7],N[8]])
A = [a,b,c]
a = sum([N[0],N[1],N[2]])
b = sum([N[3],N[4],N[5]])
c = sum([N[6],N[7],N[8]])
B = [a,b,c]
count = 0
Jiaqi = 0
while count < 9:
    print(f"{N[count]:4d}",end="")
    if count==2 or count==5 or count==8:
        print(f"{A[Jiaqi]:4d}{B[Jiaqi]:4d}")
        Jiaqi += 1
    count += 1