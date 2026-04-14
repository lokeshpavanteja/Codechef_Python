T = int(input())

for _ in range(T):
    B1, B2, B3 = map(int, input().split())
    
    empty = 0
    
    if B1 == 0:
        empty += 1
    if B2 == 0:
        empty += 1
    if B3 == 0:
        empty += 1
    
    if empty >= 2:
        print("Water filling time")
    else:
        print("Not now")