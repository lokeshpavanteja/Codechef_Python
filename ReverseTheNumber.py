T = int(input())

for _ in range(T):
    N = input()
    
    reversed_num = N[::-1]   # reverse string
    print(int(reversed_num)) # convert to int to remove leading zeros