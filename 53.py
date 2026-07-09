str_front = []
sum = 0
huanhang_count = 0
while True:
    str_latter = input()
    huanhang_count += 1
    str_front.append(str_latter)
    sum += len(str_latter)
    if sum + huanhang_count - 1 >= 10:
        break
letter = digit = other = 0
blank = huanhang_count - 1
for ch in str_front:
    for x in ch:
        if 'a' <= x.lower() <= 'z':
            letter += 1
        elif '0' <= x <= '9':
            digit += 1
        elif x == ' ':
            blank += 1
        else:
            other += 1
print("letter =", letter, end=', ')
print("blank =", blank, end=', ')
print("digit =", digit, end=', ')
print("other =", other)