import heapq
from collections import defaultdict

def dijk(s, gp):
    dists = [float("inf")] * (n + 1)
    dists[s] = 0
    hq = []
    heapq.heappush(hq, (0, s))

    while hq:

        c_dist, c_node = heapq.heappop(hq)
        if c_dist > dists[c_node]:
            continue
        nxts = gp[c_node]

        for nxt_d, nxt_node in nxts:
            new_dist = nxt_d + c_dist
            if new_dist < dists[nxt_node]:
                heapq.heappush(hq, (new_dist, nxt_node))
                dists[nxt_node] = new_dist
    return dists

n, m, x = map(int, input().split())
gp1 = defaultdict(list)
gp2 = defaultdict(list)

for _ in range(m):
    st, nd, time = map(int, input().split())
    gp1[nd].append((time, st))
    gp2[st].append((time, nd))

route = [x + y for x, y in zip(dijk(x, gp1)[1:], dijk(x, gp2)[1:])]
print(max(route))