import sys
import heapq
input = sys.stdin.readline

def dijkstra(start ,end):
    pq = [(0, start)]

    dists = [float('inf')] * (n + 1)
    dists[start] = 0
    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if cur_dist > dists[cur_node]:
            continue

        for next_node, next_weight in graph[cur_node]:
            d = dists[cur_node] + next_weight
            if d < dists[next_node]:
                dists[next_node] = d
                heapq.heappush(pq, (d, next_node))

    return dists[end]

z = int(input())
for _ in range(z):
    n, m, t = map(int, input().split()) # 교차로, 도로, 목적지 후보 개수
    s, g, h = map(int, input().split()) # 출발지
    ans = []
    graph = [[] for _ in range(n + 1)]
    candidates = []
    g_to_h = float('inf')

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
        if (a == g and b == h) or (a == h and b == g):
            g_to_h = d

    for _ in range(t):
        x = int(input())
        candidates.append(x)


    for candidate in candidates:
        path1 = dijkstra(s, g) + g_to_h + dijkstra(h, candidate)
        path2 = dijkstra(s, h) + g_to_h + dijkstra(g, candidate)
        correct_path = min(path1, path2)
        path = dijkstra(s, candidate)

        if path != float('inf') and correct_path == path:
            ans.append(candidate)
    ans.sort()
    print(*ans)