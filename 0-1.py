def fn(a,n):
    sum = 0
    term = a
    for i in range(n):
        sum += term
        term = term * 10 + a
    return sum
         
a,b=input().split()
s=fn(int(a),int(b))
print(s)