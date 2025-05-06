a, b = list(map(int, input().split()))
ans = a * b
while a > 0:
    a, b = b % a, a
print(ans // b)