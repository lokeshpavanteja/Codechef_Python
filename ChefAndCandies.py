T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    
    if X >= N:
        print(0)
    else:
        needed = N - X
        packets = (needed + 3) // 4
        print(packets)