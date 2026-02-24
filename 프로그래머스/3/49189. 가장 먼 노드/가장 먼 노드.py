from collections import defaultdict, deque

def solution(n, edges):
    dic = defaultdict(list)
    ans = defaultdict(list)
    for s, e in edges:
        dic[s].append(e)
        dic[e].append(s)
    q = deque()
    isVisited = [False] * (n + 1)
    isVisited[1] = True
    q.append((0, 1)) # idx, node
    max_idx = 0
    while q:
        idx, node = q.popleft()
        max_idx = idx
        nxts = dic[node]
        for nxt in nxts:
            if not isVisited[nxt]:
                isVisited[nxt] = True
                q.append((idx + 1, nxt))
                ans[idx].append(nxt)
    return (len(ans[max_idx - 1]))
            