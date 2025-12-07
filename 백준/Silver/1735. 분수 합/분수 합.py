def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)


a1, b1 = map(int,input().split())
a2, b2 = map(int,input().split())

child = a1 * b2 + b1 * a2
parent = b1 * b2

g = gcd(child, parent)

print(child // g, parent // g)
