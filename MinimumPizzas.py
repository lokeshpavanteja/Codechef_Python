T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    
    pizzas = (N * X + 3) // 4
    print(pizzas)