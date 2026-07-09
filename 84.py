def list_f(l=list(), cnt=1):
    res = 0
    for i in l:
        if isinstance(i, int):
            res += 1 * cnt
        else:
            res += list_f(i, cnt + 1)
    return res
print(list_f(eval(input())))
