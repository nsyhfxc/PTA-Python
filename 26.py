num = input()
dic,s="0123456789abcdefABCDEF",""
for i in num:
    if i in dic:
        s+=i
    if i == "#":
        break
if s == "":
    print(0)
else:
    Sum=int(s,16)
    if num.find("-") < num.find(s[0]):
        Sum=-Sum
    print(Sum)
