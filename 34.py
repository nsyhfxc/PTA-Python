s1 = input().strip()
s2 = input().strip()
s = ''
for i in s1:
    if s2.upper()==i.upper():
        continue
    else:
        s+=i
print(f'result: {s}')