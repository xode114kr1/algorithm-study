from itertools import combinations

def solution(line):
    
    n = len(line)
    idx_lst = [x for x in range(n)]
    spot = set()
    for comb in combinations(idx_lst, 2):
        a, b, e = line[comb[0]]
        c, d, f = line[comb[1]]
        if a * d == b * c:
            continue
        else:
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)
            if float(x).is_integer() and float(y).is_integer():
                spot.add(str(int(x)) + " " + str(int(y)))
    
    min_x, max_x = float('inf'), float('-inf')
    min_y, max_y = float('inf'), float('-inf')
    for tup in spot:
        x, y = map(int, tup.split())
        if x < min_x : min_x = x
        if x > max_x : max_x = x
        if y < min_y : min_y = y
        if y > max_y : max_y = y
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    mat = [["."] * width for _ in range(height)]
    for tup in spot:
        x, y = map(int, tup.split())
        print(x - min_x, y - min_y)
        mat[y - min_y][x - min_x] = "*"
    ans = []
    for row in mat[::-1]:
        ans.append("".join(row))
    return ans