T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    
    if max(A, C) <= B:
        print("Yes")
    else:
        print("No")