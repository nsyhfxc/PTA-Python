def iteration(lst, ceng, count):
    num = 0
    if ceng == count:
        num += len([i for i in lst if type(i) is int])
    for i in lst:
        if isinstance(i, list):
            num += iteration(i, ceng, count+1)
    return num
print(iteration(eval(input()), eval(input()), 1))