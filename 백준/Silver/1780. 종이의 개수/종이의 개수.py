n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
dic = {-1:0, 0:0, 1:0}


def count_paper(x1, x2, y1, y2):
    first_num = mat[x1][y1]
    is_same = True
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if mat[x][y] != first_num:
                is_same = False
                break
        if not is_same : break

    if is_same:
        dic[first_num] += 1

    else:
        new_size = (x2 - x1 + 1) // 3
        mx1 = x1 + new_size - 1
        my1 = y1 + new_size - 1
        mx2 = mx1 + new_size
        my2 = my1 + new_size
        count_paper(x1, mx1, y1, my1)
        count_paper(x1, mx1, my1 + 1, my2)
        count_paper(x1, mx1, my2 + 1, y2)
        # my1 + 1, my2
        count_paper(mx1 + 1, mx2, y1, my1)
        count_paper(mx1 + 1, mx2, my1 + 1, my2)
        count_paper(mx1 + 1, mx2, my2 + 1, y2)
        # my2 + 1, y2
        count_paper(mx2 + 1, x2, y1, my1)
        count_paper(mx2 + 1, x2, my1 + 1, my2)
        count_paper(mx2 + 1, x2, my2 + 1, y2)


count_paper(0, n - 1, 0, n - 1)
for k in [-1,0,1]:
    print(dic[k])