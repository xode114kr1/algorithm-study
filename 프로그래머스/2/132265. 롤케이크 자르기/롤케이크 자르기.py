from collections import defaultdict

def solution(topping):
    ans = 0
    dic = defaultdict(int)
    set_a = set()
    set_b = set()
    
    for t in topping:
        dic[t] += 1
        set_b.add(t)
    
    for t in topping:
        set_a.add(t)
        dic[t] -= 1
        if dic[t] == 0:
            set_b.remove(t)
        if len(set_a) == len(set_b):
            ans += 1
    return ans