T = int(input())

for _ in range(T):
    N = int(input())
    D = list(map(int, input().split()))
    
    remove = 0
    
    for d in D:
        if d >= 1000:
            remove += 1
    
    print(remove)