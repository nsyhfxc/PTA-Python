word_times=dict()
cnt_word=0
flag=True
while flag:
    string = input()
    string = string.lower()
    flag = string.find("#")==-1
    for x in string:
        if x.isalnum()==False and x!="_" and x!="#":
            string = string.replace(x, " ")
    string = string.split("#")[0].split()
    for i in range(len(string)):
        if string[i]!="":
            string[i]=string[i][:15]
            if string[i] in word_times.keys():
                word_times[string[i]]+=1
            else:
                word_times[string[i]]=1
                cnt_word+=1
word_times=sorted(word_times.items(),key=lambda x:(-x[1],x[0]))
print(cnt_word)
for i in range(cnt_word//10):
    print("%s:%s"%(word_times[i][1],word_times[i][0]))
