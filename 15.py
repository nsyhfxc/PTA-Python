from math import sqrt
a,b,c = map(eval,input().split())
p = (a + b + c) / 2
area = sqrt(abs(p * (p - a) * (p - b) * (p - c)))
perimeter = a + b + c
if(a + b > c and a + c > b and b + c > a):
    print(f"area = {area:.2f}; perimeter = {perimeter:.2f}")
else:
    print("These sides do not correspond to a valid triangle")