def find_idx(r, c):
    if r == 0 and c == 0:
        return 1
    degree = max(abs(r), abs(c))
    st_idx = (degree - 1) * (16 + (degree - 2) * 8) // 2 + 2
    st_r, st_c = degree - 1, degree
    if r <= degree - 1 and c == degree:
        return st_idx + (degree - 1 - r)
    elif r == -1 * degree:
        st = st_idx + 2 * degree - 1
        return st + (degree - c)
    elif c == -1 * degree:
        st = st_idx + 4 * degree - 1
        return st + (degree + r)
    else:
        st = st_idx + 6 * degree - 1
        return st + (degree + c)


r1, c1, r2, c2 = map(int, input().split())

max_val = 0
for r in range(r1, r2 + 1):
    for c in range(c1, c2 + 1):
        max_val = max(max_val, find_idx(r, c))
width = len(str(max_val))

for r in range(r1, r2 + 1):
    for c in range(c1, c2 + 1):
        print(str(find_idx(r, c)).rjust(width), end=" ")
    print()
