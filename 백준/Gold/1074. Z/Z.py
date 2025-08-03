cnt = 0

direction = [(0, 0), (0, 1), (1, 0), (1, 1)]
def z(n, x, y):
    global cnt
    if n == 0:
        if x == c and y == r:
            print(cnt)
            exit()
        cnt += 1
        return

    size = 2 ** (n - 1)

    if c < x + size and r < y + size:
        z(n - 1, x, y)
    elif c >= x + size and r < y + size:
        cnt += size * size
        z(n - 1, x + size, y)
    elif c < x + size and r >= y + size:
        cnt += 2 * size * size
        z(n - 1, x, y + size)
    else:
        cnt += 3 * size * size
        z(n - 1, x + size, y + size)

N, r, c = map(int, input().split())
z(N, 0, 0)