str = input()
flag = 1
for i in range(0,int(len(str)/2)):
    if(str[i] != str[len(str) - 1 - i]):
        flag = 0
if(flag == 1):
    print(str)
    print("Yes")
else:
    print(str)
    print("No")
exit(0)
