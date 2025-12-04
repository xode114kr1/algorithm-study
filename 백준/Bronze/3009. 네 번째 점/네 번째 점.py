xs = []
ys = []

for _ in range(3):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

for x in xs:
    if xs.count(x) == 1:
        x4 = x
        break

for y in ys:
    if ys.count(y) == 1:
        y4 = y
        break

print(x4, y4)
