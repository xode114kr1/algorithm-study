from collections import deque

def find_c(C):
    lst = []
    for i in range(r):
        for j in range(c):
            if mat[i][j] == C:
                lst.append([i, j])
    return lst

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

r, c = map(int, input().split())
mat = [list(input()) for _ in range(r)]

human = find_c("J")[0]
fires = find_c("F")

fq = deque()
fire_cnt = [[-1] * c for _ in range(r)]
for fx, fy in fires:
    fq.append((fx, fy, 0)) # x, y, cnt
    fire_cnt[fx][fy] = 0

while fq:
    cx, cy, ccnt = fq.popleft()
    for dx, dy in direction:
        nx, ny = cx + dx, cy + dy
        if not (0 <= nx < r) or not (0 <= ny < c):
            continue
        if mat[nx][ny] != "#" and fire_cnt[nx][ny] == -1:
            fq.append((nx, ny, ccnt + 1))
            fire_cnt[nx][ny] = ccnt + 1

q = deque()
isVisited = [[False] * c for _ in range(r)]

q.append((human[0], human[1], 0))
isVisited[human[0]][human[1]] = True
while q:
    cx, cy, ccnt = q.popleft()

    if cx == 0 or cx == r - 1 or cy == 0 or cy == c - 1:
        print(ccnt + 1)
        exit()

    for dx, dy in direction:
        nx, ny = cx + dx, cy + dy
        if not (0 <= nx < r) or not (0 <= ny < c):
            continue
        if mat[nx][ny] == "#" or isVisited[nx][ny] :
            continue
        if fire_cnt[nx][ny] == -1 or ccnt + 1 < fire_cnt[nx][ny]:
            q.append((nx, ny, ccnt + 1))
            isVisited[nx][ny] = True

print("IMPOSSIBLE ")