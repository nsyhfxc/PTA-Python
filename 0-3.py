def CountDigit(number, digit):
    number = int(abs(number))
    cnt = 0
    while(number):
        if number % 10 == digit:
            cnt += 1
        number //= 10
    return cnt
        
number, digit = input().split()
number = int(number)
digit = int(digit)
count = CountDigit(number, digit)
print("Number of digit", digit, "in", str(number) + ":", count)