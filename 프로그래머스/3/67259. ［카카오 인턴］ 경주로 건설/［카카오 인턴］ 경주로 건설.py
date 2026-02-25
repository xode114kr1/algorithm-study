import heapq

def solution(board):
    n = len(board)
    direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    isVisited = [[-1] * n for _ in range(n)]
    hq = [(0, 0, 0)] # cnt, x, y, d
    best = float('inf')
    while hq:
        cnt, x, y = heapq.heappop(hq)
        
        if x == n - 1 and y == n - 1:
            best = min(best, cnt - 500)
        
        for dx, dy in direction:
            i = 1
            while 1:
                nx, ny = x + dx * i, y + dy * i
                if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] == 1:
                    break
                ncnt = cnt + 500 + 100 * i
                if isVisited[nx][ny] != -1 and isVisited[nx][ny] <= ncnt:
                    i += 1
                    continue
                
                isVisited[nx][ny] = ncnt
                heapq.heappush(hq, (ncnt, nx, ny))
                i += 1
    return best