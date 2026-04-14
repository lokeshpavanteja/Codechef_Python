T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    
    bags = (X * Y) // 100
    print(bags)