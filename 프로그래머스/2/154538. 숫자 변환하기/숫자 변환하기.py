from collections import deque

def solution(x, y, n):
    dist = [-1] * (y + 1)
    dist[x] = 0
    q = deque()
    q.append((x, 0))
    while q:
        cur, cnt = q.popleft()
        if cur == y:
            return cnt
        
        if cur * 3 <= y and dist[cur * 3] == -1:
            dist[cur * 3] = dist[cur] + 1
            q.append((cur * 3, cnt + 1))
        if cur * 2 <= y and dist[cur * 2] == -1:
            dist[cur * 2] = dist[cur] + 1
            q.append((cur * 2, cnt + 1))
        if cur + n <= y and dist[cur + n] == -1:
            dist[cur + n] = dist[cur] + 1
            q.append((cur + n, cnt + 1))
    return -1