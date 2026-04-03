import heapq
import sys
from heapq import heappush

input = sys.stdin.readline
loof_cnt = 1
while 1:
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    n = int(input())
    if n == 0:
        break
    mat = [list(map(int, input().split())) for _ in range(n)]
    cnt_mat = [[float('inf')] * n for _ in range(n)]
    cnt_mat[0][0] = mat[0][0]
    q = []  # x, y, cnt
    heapq.heappush(q, (mat[0][0], 0, 0))
    while q:
        cnt, cx, cy = heapq.heappop(q)
        for dx, dy in direction:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            n_cnt = cnt + mat[nx][ny]
            if n_cnt < cnt_mat[nx][ny]:
                cnt_mat[nx][ny] = n_cnt
                heappush(q, (n_cnt, nx, ny))
    print(f"Problem {loof_cnt}: {cnt_mat[n - 1][n - 1]}")
    loof_cnt += 1