def f(item):
    for i in item:
        if type(i) is list or type(i) is tuple:
            f(i)
        elif type(i) is int or type(i) is float:
            lsts.append(i)
lst = eval(input())
lsts = list()
f(lst)
print(sum(lsts))