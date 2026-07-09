s = list(input())
s_ = []
k = 0
for i in range(0,len(s)):
    if s[i] not in s_:
        if 'a'<= s[i] <='z' and (chr(ord(s[i])-32) not in s_):
            s_.append(s[i])
            k+=1
        if ('A'<= s[i] <= 'Z') and (chr(ord(s[i])+32) not in s_):
            s_.append(s[i])
            k+=1
    if k == 10:
        break
if k == 10:
    print(''.join(s_))
else:
    print("not found")