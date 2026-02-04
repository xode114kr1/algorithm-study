from collections import deque

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution(places):
    ans = []
    for place in places:
        n, m = len(place), len(place[0])

        def bfs(sx, sy):
            isVisited = [[False] * m for _ in range(n)]
            q = deque()
            q.append([sx, sy, 0])
            isVisited[sx][sy] = True
            while q:
                cx, cy, cnt = q.popleft()
                for dx, dy in direction:
                    nx, ny = cx + dx, cy + dy
                    if nx < 0 or ny < 0 or nx >= n or ny >= m : continue
                    if not isVisited[nx][ny] and place[nx][ny] != "X":
                        if place[nx][ny] == "P" and cnt <= 1: 
                            return False
                        isVisited[nx][ny] = True
                        q.append([nx, ny, cnt + 1])

            return True
        ok = True
        for i in range(n):
            if not ok : break
            for j in range(m):
                if place[i][j] == "P":
                    if not bfs(i, j):
                        ok = False
                        break
        ans.append(int(ok))
    return ans