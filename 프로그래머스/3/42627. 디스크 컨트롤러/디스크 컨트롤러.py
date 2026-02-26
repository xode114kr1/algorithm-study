import heapq

def solution(jobs):
    jobs.sort()
    
    n = len(jobs)
    time = 0
    idx = 0
    hq = []
    ans = 0
    
    while idx < n or hq:
        while idx < n:
            s, d = jobs[idx]
            if s <= time:
                heapq.heappush(hq, [d, s])
                idx += 1
            else:
                break
        
        if hq:
            d, s = heapq.heappop(hq)
            time += d
            ans += time - s
        else:
            time = jobs[idx][0]
            
    return ans // n
    
    