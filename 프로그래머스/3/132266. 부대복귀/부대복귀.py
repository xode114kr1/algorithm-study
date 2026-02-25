# import 
from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    def dijk(start):
        dists = [-1] * (n + 1)
        dists[start] = 0
        q = deque()
        q.append([0, start])
        
        while q:
            cnt, cur = q.popleft()
            nxts = dic[cur]
            
            for nxt in nxts:
                if dists[nxt] == -1:
                    dists[nxt] = cnt + 1
                    q.append([cnt + 1, nxt])
        return (dists)
                
    
    dic = defaultdict(list)
    for s, e in roads:
        dic[s].append(e)
        dic[e].append(s)
    
    d = dijk(destination)
    ans = []
    for s in sources:
        ans.append(d[s])
    return ans