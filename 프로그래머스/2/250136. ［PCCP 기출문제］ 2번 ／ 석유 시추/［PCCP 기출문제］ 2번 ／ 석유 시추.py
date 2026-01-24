from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

def solution(land):
    n, m = len(land), len(land[0])
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    isVisited = [[False] * m for _ in range(n)]

    def dfs(x, y, i):
        land_sizes[i] += 1
        land_ys[i].add(y)
        dic[y].add(i)
        isVisited[x][y] = True
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if land[nx][ny] == 1 and not isVisited[nx][ny]:
                dfs(nx, ny, i)

    land_sizes = []
    land_ys = []
    dic = defaultdict(set)
    land_idx = 0
    for i in range(n):
        for j in range(m):
            if isVisited[i][j] or land[i][j] == 0: continue
            land_sizes.append(0)
            land_ys.append(set())
            dfs(i, j, land_idx)
            land_idx += 1

    ans = 0
    for key, val in dic.items():
        cnt = 0
        for idx in val:
            cnt += land_sizes[idx]
        ans = max(ans, cnt)
    return ans