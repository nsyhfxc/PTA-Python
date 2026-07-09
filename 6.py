x = eval(input())
y = 0
if(x < 0):
    print("Invalid Value!")
elif(x <= 50):
    y = x * 0.53
    print(f"cost = {y:.2f}")
else:
    y = 0.53 * 50 + (x - 50) * (0.53 + 0.05)
    print(f"cost = {y:.2f}")
