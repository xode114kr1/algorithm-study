def solution(k, ranges):
    areas = [] # i : i ~ i + 1의 넓이
    cur = k
    while cur != 1:
        nxt = cur // 2 if cur % 2 == 0 else cur * 3 + 1
        areas.append((cur + nxt) / 2)
        cur = nxt
    
    n = len(areas)
    
    prefixs = [0.0]
    prefix = 0.0
    for area in areas:
        prefix += area
        prefixs.append(prefix)

    ans = []
    
    for s, off in ranges:
        e = n + off
        
        if e >= s:
            ans.append(prefixs[e] - prefixs[s])
        else:
            ans.append(-1)
        
    return ans