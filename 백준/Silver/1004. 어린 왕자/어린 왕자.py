t = int(input())

def is_in(x, y, cx, cy, r):
    return (x - cx) ** 2 + (y - cy) ** 2 < r ** 2

for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    start_cnt = 0
    end_cnt = 0
    for cx, cy, r in lst:
        if is_in(x1, y1, cx, cy, r) ^ is_in(x2, y2, cx, cy, r): start_cnt += 1
    print(start_cnt + end_cnt)