import heapq

def solution(n, start, a, b, fares):
    def dijk(s):
        dist = [float('inf')] * (n + 1)
        dist[s] = 0
        hq = [(0, s)]
        
        while hq:
            cur_dist, cur_node = heapq.heappop(hq)
            
            if cur_dist > dist[cur_node]:
                continue
            
            for nxt_node, w in graph[cur_node]:
                nd = cur_dist + w
                
                if nd < dist[nxt_node]:
                    dist[nxt_node] = nd
                    heapq.heappush(hq, (nd, nxt_node))
        return dist
        
    
    graph = [[] for _ in range(n + 1)]
    for s, e, d in fares:
        graph[s].append((e, d))
        graph[e].append((s, d))
    
    s_dist = dijk(start)
    a_dist = dijk(a)
    b_dist = dijk(b)
    
    ans = float("inf")
    for k in range(1, n + 1):
        cost = s_dist[k] + a_dist[k] + b_dist[k]
        ans = min(ans, cost)
    return ans
    
    