from collections import deque
import heapq
n, k = map(int, input().split())

if n >= k :
    print(n - k)
    exit()

dp_size: int = (2 * k + 1)
dp = [float('inf')] * dp_size

pq = [(0, n)]

while pq:
    cnt, cur = heapq.heappop(pq)

    if cur == k:
        print(cnt)
        break

    if cur - 1 >= 0 and cnt + 1 < dp[cur - 1]:
        dp[cur - 1] = cnt + 1
        heapq.heappush(pq, (cnt + 1, cur - 1))


    if cur + 1 < dp_size and cnt + 1 < dp[cur + 1]:
        dp[cur + 1] = cnt + 1
        heapq.heappush(pq, (cnt + 1, cur + 1))


    idx = cur * 2
    if idx == 0: continue
    while idx < dp_size:
        if cnt < dp[idx]:
            dp[idx] = cnt
            heapq.heappush(pq, (cnt, idx))
        idx *= 2
