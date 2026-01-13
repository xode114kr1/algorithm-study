from collections import deque

start, end = map(int, input().split())
max_idx = max(start, end) * 2


q = deque()
lst = [float("inf")] * (max_idx + 1)
lst[start] = 0
isVisited = [False] * (max_idx + 1)
isVisited[start] = True
q.append([start, 0])

while 1:
    cur = q.popleft()
    idx, cnt = cur[0], cur[1]

    if idx == end:
        print(cnt)
        break

    if idx - 1 >= 0 and lst[idx - 1] > cnt + 1:
        q.append([idx - 1, cnt + 1])
        lst[idx - 1] = cnt + 1

    if idx + 1 <= max_idx and lst[idx + 1] > cnt + 1:
        q.append([idx + 1, cnt + 1])
        lst[idx + 1] = cnt + 1
    if idx * 2 <= max_idx and lst[idx * 2] > cnt + 1:
        q.append([idx * 2, cnt + 1])
        lst[idx * 2] = cnt + 1



