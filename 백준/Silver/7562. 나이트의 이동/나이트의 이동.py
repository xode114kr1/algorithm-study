import sys
from collections import deque
input = sys.stdin.readline

direction = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
z = int(input())
for _  in range(z):
    size = int(input())
    mat = [[float("inf")] * size for _ in range(size)]
    isVisited = [[False] * size for _ in range(size)]

    q = deque()

    s_x, s_y = map(int, input().split())
    e_x, e_y = map(int, input().split())

    mat[s_x][s_y] = 0
    isVisited[s_x][s_y] = True
    q.append([s_x, s_y, 0])

    while 1:
        cur = q.popleft()
        cur_x, cur_y, cnt = cur[0], cur[1], cur[2]

        if cur_x == e_x and cur_y == e_y:
            print(cnt)
            break

        for dx, dy in direction:
            nx = cur_x + dx
            ny = cur_y + dy
            if nx < 0 or ny < 0 or nx >= size or ny >= size:
                continue
            if mat[nx][ny] > cnt + 1:
                q.append([nx, ny, cnt + 1])
                mat[nx][ny] = cnt + 1
