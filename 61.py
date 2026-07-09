n,a,b,c = int(input()),[],[],1
for I in range(n):
    a.append(list(map(int,input().split())))
for J in  range(n):
    b.append([])
    for j in range(n):
        b[J].append(a[j][J])
for I in range(n):
    for i in range(n):
        if max(a[I]) == min(b[i]):
            print(f'{I} {i}')
            c = 0
if c:
    print('NONE')