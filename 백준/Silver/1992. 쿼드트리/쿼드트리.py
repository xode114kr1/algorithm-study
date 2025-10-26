import math

def quad_tree(x1, x2, y1, y2):
    first_num = mat[x1][y1]
    is_same = True
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if mat[x][y] != first_num:
                is_same = False

    if is_same:
        return first_num

    mx = (x1 + x2) // 2
    my = (y1 + y2) // 2
    return "(" \
        + quad_tree(x1, mx, y1, my) \
        + quad_tree(x1, mx, my + 1, y2) \
        + quad_tree(mx + 1, x2, y1, my) \
        + quad_tree(mx + 1, x2, my + 1, y2) \
        + ")"

n = int(input())
mat = [list(input()) for _ in range(n)]

print(quad_tree(0, n - 1, 0, n - 1))
