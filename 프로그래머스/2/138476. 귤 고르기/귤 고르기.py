from collections import defaultdict

def solution(k, tangerine):
    d = defaultdict(int)
    for t in tangerine:
        d[t] += 1
    lst = list(d.values())
    lst.sort(key = lambda x :-x)
    ans = 0
    cnt = 0
    for num in lst:
        cnt += num
        ans += 1
        if cnt >= k:
            return ans