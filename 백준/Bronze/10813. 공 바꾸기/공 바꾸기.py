n, m = map(int, input().split())
basket = [i for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    basket[a], basket[b] = basket[b], basket[a]

print(*basket[1:])
