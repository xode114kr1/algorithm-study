from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    dic = defaultdict(int)
    max_len = 0
    
    for order in orders:
        max_len = max(max_len, len(order))
        for i in range(2, len(order) + 1):
            for comb in combinations(order, i): 
                menu = "".join(sorted(comb))
                dic[menu] += 1
    
    ans = []
    count = [0] * (max_len + 1)
    for k, v in dic.items():
        n = len(k)
        count[n] = max(count[n], v)
    
    
    for k, v in dic.items():
        n = len(k)
        if n in course and v == count[n] and v > 1:
            ans.append(k)
    ans.sort()
    return ans