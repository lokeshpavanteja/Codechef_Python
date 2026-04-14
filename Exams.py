T = int(input())

for _ in range(T):
    X, Y, Z = map(int, input().split())
    
    if 2 * Z > X * Y:
        print("YES")
    else:
        print("NO")