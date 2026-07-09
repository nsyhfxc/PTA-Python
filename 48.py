n = list(map(int,input().split()))
price = [3,2.5,4.1,10.2]
print("[1] apple\n[2] pear\n[3] orange\n[4] grape\n[0] exit")
for i in range(5):
    if n[i] == 0 :
        break
    elif n[i] < 0 or n[i]>4:
        print("price = 0.00")
    else:
        print(f"price = {price[n[i]-1]:.2f}")