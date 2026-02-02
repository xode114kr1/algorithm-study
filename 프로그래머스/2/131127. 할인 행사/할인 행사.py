from collections import defaultdict

def solution(want, number, discount):
    def all_zero(lst):
        for num in lst:
            if num != 0:return False
        return True
    
    dic = dict()
    want_set = set(want)
    for w, n in zip(want, number):
        dic[w] = n
    
    
    for i in range(10):
        cur = discount[i]
        if cur in want_set:
            dic[cur] -= 1
    
    ans = 0
    if all_zero(dic.values()) : ans += 1
    
    for i in range(10, len(discount)):
        added = discount[i]
        removed = discount[i - 10]
        if added in want_set:
            dic[added] -= 1
        if removed in want_set:
            dic[removed] += 1
        if all_zero(dic.values()) : ans += 1
    return ans
        