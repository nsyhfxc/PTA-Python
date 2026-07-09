def cmp(lst):
    if str(lst[0]) == lst[0]:
        return ord(lst[0])
    else:
        return lst[0]
dct = eval(input())
dct1 = eval(input())
for i in dct1:
    if i in dct:
        dct[i] += dct1[i]
    else:
        dct.update({i:dct1[i]})
lst = [[i,dct[i]] for i in dct]
lst = sorted(lst,key = cmp,reverse = False)
dct = {k:v for k,v in lst}
ans = str(dct).replace(' ','').replace("'",'"')
print(ans)