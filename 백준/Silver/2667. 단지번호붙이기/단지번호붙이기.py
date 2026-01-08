n = int(input())
mat = [list(map(int, list(input()))) for _ in range(n)]
isVisited = [[False for _ in range(n)] for _ in range(n)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ans = []
cnt = 0
def dfs(r, c):
    global cnt
    isVisited[r][c] = True
    cnt += 1
    for dx, dy in direction:
        nr = r + dx
        nc = c + dy
        if nr < 0 or nc < 0 or nr >= n or nc >= n : continue

        if mat[nr][nc] == 1 and not isVisited[nr][nc]:
            dfs(nr, nc)

for row in range(n):
    for col in range(n):
        cnt = 0
        if mat[row][col] == 0 or isVisited[row][col]: continue
        dfs(row, col)
        ans.append(cnt)

ans.sort()
print(len(ans))
for i in ans:
    print(i)