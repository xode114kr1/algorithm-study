from collections import defaultdict, deque

n, m, r = map(int, input().split())
dic = defaultdict(list)
isVisited = [False] * (n + 1)
cnt = 1
ans = [0] * (n + 1)
for _ in range(m):
    start, end = map(int, input().split())
    dic[start].append(end)
    dic[end].append(start)

for i in range(1, n + 1):
    dic[i].sort(reverse=True)

q = deque()
q.append(r)
isVisited[r] = True
while q:
    cur = q.popleft()

    ans[cur] = cnt

    for node in dic[cur]:
        if isVisited[node]: continue
        q.append(node)
        isVisited[node] = True
    cnt += 1
for node in ans[1:]:
    print(node)