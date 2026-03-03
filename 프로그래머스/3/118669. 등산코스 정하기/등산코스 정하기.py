from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    def dijk():
        dists = [float('inf')] * (n + 1)
        hq = []
        for gate in gates:
            dists[gate] = 0
            heapq.heappush(hq, (0, gate))
        
        
        while hq:
            d, cur = heapq.heappop(hq)
            
            if d > dists[cur]:
                continue
            
            nxts = gp[cur]
            for nxt, w in nxts:
                nd = max(d, w)
                if nd < dists[nxt]:
                    dists[nxt] = nd
                    if nxt not in s_set:
                        heapq.heappush(hq, (nd, nxt))
                    
        return dists
        
    
    gp = defaultdict(list)
    
    for s, e, d in paths:
        gp[s].append([e, d])
        gp[e].append([s, d])
    
    gate_dists = {}
    s_set = set(summits)
    
    dist = dijk()
    
    best_summit = None
    best_intensity = float('inf')
    
    for s in sorted(summits):
        if dist[s] < best_intensity:
            best_intensity = dist[s]
            best_summit = s
             
    return [best_summit, best_intensity]
    