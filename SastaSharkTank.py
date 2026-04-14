T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    
    if 2 * A > B:
        print("FIRST")
    elif 2 * A < B:
        print("SECOND")
    else:
        print("ANY")