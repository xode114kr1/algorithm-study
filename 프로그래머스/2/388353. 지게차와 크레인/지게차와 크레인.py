from collections import deque


def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def isCanCar(new_mat, x, y):
        q = deque()
        q.append((x, y))
        isVisited = [[False] * m for _ in range(n)]
        isVisited[x][y] = True

        while q:
            i, j = q.popleft()

            if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                return True

            for dx, dy in direction:
                nx = dx + i
                ny = dy + j
                if nx < 0 or ny < 0 or nx >= n or ny >= m: continue

                if not isVisited[nx][ny] and new_mat[nx][ny] == 0:
                    isVisited[nx][ny] = True
                    q.append((nx, ny))
        return False

    def car(new_mat, c):
        for i in range(n):
            for j in range(m):
                if mat[i][j] == c:
                    if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                        new_mat[i][j] = 0
                    elif isCanCar(mat, i, j):
                        new_mat[i][j] = 0
        return new_mat

    def crain(new_mat, c):
        for i in range(n):
            for j in range(m):
                if new_mat[i][j] == c:
                    new_mat[i][j] = 0

        return new_mat

    mat = [list(row) for row in storage]

    for req in requests:
        if len(req) == 1:
            mat = car([list(row) for row in mat], req)
        else:
            mat = crain([list(row) for row in mat], req[0])

    ans = 0
    for row in mat:
        for cell in row:
            if cell != 0:
                ans += 1

    return ans