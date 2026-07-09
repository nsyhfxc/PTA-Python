a = eval(input())
n = input()
b = eval(input())
if n == '+':
    print(f"{(a + b):.2f}")
elif n == '-':
    print(f"{(a - b):.2f}")
elif n == '*':
    print(f"{(a * b):.2f}")
else:
    if(not b):
        print("divided by zero")
    else:
        print(f"{(a / b):.2f}")