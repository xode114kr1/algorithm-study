from collections import deque, defaultdict

n, m = map(int, input().split())

dic = defaultdict(int)
dp = [float('inf')] * 101
for _ in range(n + m):
    start, end = map(int, input().split())
    dic[start] = end

q = deque()
q.append([1, 0])
while 1:
    cur = q.popleft()
    idx, cnt = cur[0], cur[1]

    if idx == 100:
        print(cnt)
        break

    for i in range(1, 7):
        nxt = idx + i
        if nxt > 100: break

        if dic[nxt] == 0 and dp[nxt] > cnt + 1:
            q.append([nxt, cnt + 1])
            dp[nxt] = cnt + 1
        elif dic[nxt] != 0 and dp[dic[nxt]] > cnt + 1:
            q.append([dic[nxt], cnt + 1])
            dp[dic[nxt]] = cnt + 1
