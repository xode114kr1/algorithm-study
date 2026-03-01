def print_mat(mat):
    for row in mat:
        print(*row)

def solution(key, lock):
    def ok(k, l, sx, sy):
        l = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                l[i][j] = lock[i][j]
        
        for x in range(n):
            for y in range(n):
                nx, ny = sx + x, sy + y
                if 0 <= nx < m and 0 <= ny < m:
                    l[sx + x][sy + y] += k[x][y]

        for row in l:
            for cell in row:
                if cell != 1: return False
            
        return True
    
    n = len(key)
    m = len(lock)
    key1 = [[0] * n for _ in range(n)]
    key2 = [[0] * n for _ in range(n)]
    key3 = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            key1[j][-i - 1] = key[i][j]
            key2[-i - 1][-j - 1] = key[i][j]
            key3[-j - 1][i] = key[i][j]

    for i in range(-(n - 1), m):
        for j in range(-(n - 1), m):
            if ok(key, lock, i, j):
                return True
            if ok(key1, lock, i, j):
                return True
            if ok(key2, lock, i, j):
                return True
            if ok(key3, lock, i, j):
                return True
    return False