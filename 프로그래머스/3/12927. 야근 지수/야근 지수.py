import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    h = []
    for work in works:
        heapq.heappush(h, -work)
    for _ in range(n):
        x = -heapq.heappop(h)
        x -= 1
        heapq.heappush(h, -x)
    ans = 0
    for x in h:
        ans += x ** 2
    return ans
    
    