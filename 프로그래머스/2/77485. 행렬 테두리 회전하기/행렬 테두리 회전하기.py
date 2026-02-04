def solution(rows, columns, queries):
    mat = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            mat[i][j] = i * columns + j + 1
    ans = []
    for query in queries:
        small_num = float('inf')
        query = [x - 1 for x in query.copy()]
        
        x1, y1, x2, y2 = query
        before = mat[x1][y1]
        for y in range(y1 + 1, y2 + 1):
            cur = mat[x1][y]
            small_num = min(small_num, cur)
            mat[x1][y] = before
            before = cur
            
        for x in range(x1 + 1, x2 + 1):
            cur = mat[x][y2]
            small_num = min(small_num, cur)
            mat[x][y2] = before
            before = cur
            
        for y in range(y2 - 1, y1 - 1, -1):
            cur = mat[x2][y]
            small_num = min(small_num, cur)
            mat[x2][y] = before
            before = cur

        for x in range(x2 - 1, x1 - 1, -1):
            cur = mat[x][y1]
            small_num = min(small_num, cur)
            mat[x][y1] = before
            before = cur
        ans.append(small_num)
        
    return ans