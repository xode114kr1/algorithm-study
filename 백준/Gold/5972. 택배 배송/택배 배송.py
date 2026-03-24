import heapq

def dijk():
    dist = [float('inf')] * (n + 1)
    dist[1] = 0

    hq = []
    heapq.heappush(hq, [0, 1])

    while hq:
        cur_cnt, cur_node = heapq.heappop(hq)

        if cur_cnt > dist[cur_node]:
            continue

        nxts = graph[cur_node]

        for nxt_node, d in nxts:
            nxt_cnt = cur_cnt + d
            if nxt_cnt < dist[nxt_node]:
                dist[nxt_node] = nxt_cnt
                heapq.heappush(hq, [nxt_cnt, nxt_node])
    return dist


n, m = map(int ,input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))
    graph[e].append((s, d))
print(dijk()[-1])