s = input()
res = []
for ch in s:
    if(ch.isupper() and ch not in res):
        res.append(ch)
if(len(res) == 0):
    print("Not Found")
else:
    for c in res:
        print(c,end="")
