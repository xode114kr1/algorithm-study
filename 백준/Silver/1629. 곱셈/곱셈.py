a, b, c = map(int, input().split())

def mod_pow(a, n, m):
    if n == 0:
        return 1 % m
    if n == 1:
        return a % m
    half = mod_pow(a, n // 2, m)
    res = (half * half) % m
    if n % 2 == 1: 
        res = (res * a) % m
    return res

print(mod_pow(a % c, b, c))