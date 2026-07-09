num = input()
dic,count="AEIOU",0
for i in num:
    if i not in dic and (i>="A" and i<="Z"):
        count+=1
print(count)
