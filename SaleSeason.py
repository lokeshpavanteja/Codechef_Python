T = int(input())

for _ in range(T):
    X = int(input())
    
    if X <= 100:
        discount = 0
    elif X <= 1000:
        discount = 25
    elif X <= 5000:
        discount = 100
    else:
        discount = 500
    
    print(X - discount)