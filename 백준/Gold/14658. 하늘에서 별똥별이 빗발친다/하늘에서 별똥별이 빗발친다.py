from itertools import product

n, m, l, k = map(int, input().split()) # 가로, 세로, 트램펄린, 별동별

cand_x = set()
cand_y = set()
lst = []
for _ in range(k):
    x, y = map(int, input().split())
    cand_x.add(x)
    cand_y.add(y)
    lst.append((x, y))

max_block = 0
for sx, sy in product(cand_x, cand_y):
    cnt = 0
    ex, ey = sx + l, sy + l
    for x, y in lst:
        if sx <= x <= ex and sy <= y <= ey:
            cnt += 1
    max_block = max(max_block, cnt)
print(k - max_block)