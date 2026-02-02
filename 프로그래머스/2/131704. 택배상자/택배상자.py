from collections import deque

def solution(order):
    n = len(order)
    cur_box = 1
    sub = []
    ans = []
    for num in order:
        while cur_box <= n and cur_box < num:
            sub.append(cur_box)
            cur_box += 1
            
        if cur_box == num:
            ans.append(cur_box)
            cur_box += 1
        elif sub and sub[-1] == num:
            ans.append(sub.pop())
        else:
            break
    return len(ans)
        
    
        