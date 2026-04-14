T = int(input())

for _ in range(T):
    A, B, X, Y = map(int, input().split())
    
    if X * Y >= A * B:
        print("Yes")
    else:
        print("No")