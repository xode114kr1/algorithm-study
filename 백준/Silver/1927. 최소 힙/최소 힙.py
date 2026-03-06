import sys
input = sys.stdin.readline

import heapq

n = int(input())
hq = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if len(hq) == 0:
            print(0)
        else:
            p = heapq.heappop(hq)
            print(p)
    else:
        heapq.heappush(hq, num)
