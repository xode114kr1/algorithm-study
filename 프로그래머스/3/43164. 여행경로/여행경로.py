from collections import defaultdict

def solution(tickets):
    def dfs(cur):
        if len(route) == n + 1:
            return True
        
        nxts = dic[cur]
        for i in range(len(nxts)):
            nxt = nxts[i]
            if nxt is None:
                continue
            
            nxts[i] = None
            route.append(nxt)
            if dfs(nxt):
                return True
            
            route.pop()
            nxts[i] = nxt
        return False
    
    n = len(tickets)
    
    dic = defaultdict(list)
    for s, e in tickets:
        dic[s].append(e)
    for key in dic:
        dic[key].sort()
        
    route = ["ICN"]
    dfs("ICN")
    return (route)