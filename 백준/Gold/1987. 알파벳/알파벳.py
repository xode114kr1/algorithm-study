import sys
input = sys.stdin.readline

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y, cnt):
    global ans
    if cnt > ans:
        ans = cnt

    if ans == 26:
        return

    for dx, dy in direction:
        nx, ny = x + dx, y + dy

        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue

        idx = board[nx][ny]
        if not visited[idx]:
            visited[idx] = True
            dfs(nx, ny, cnt + 1)
            visited[idx] = False

r, c = map(int, input().split())
mat = [input().strip() for _ in range(r)]

board = [[ord(ch) - 65 for ch in row] for row in mat]
visited = [False] * 26

ans = 0
visited[board[0][0]] = True
dfs(0, 0, 1)

print(ans)