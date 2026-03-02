def solution(n, m, x, y, r, c, k):
    x_gap = r - x
    y_gap = c - y
    
    cur_x, cur_y = x, y
    gap = abs(x_gap) + abs(y_gap)
    rest = k - gap
    ans = ""
    
    dic = {"d" : 0, "l" : 0, "r" : 0, "u" : 0}
    if x_gap > 0:
        dic["d"] += x_gap
    else:
        dic["u"] -= x_gap
    
    if y_gap > 0:
        dic["r"] += y_gap
    else:
        dic["l"] -= y_gap
    
    if rest % 2 == 1 or rest < 0:
        return "impossible"
    
    ans += "d" * dic["d"]
    cur_x += dic["d"]
    
    can_down = min(n - cur_x, rest // 2)
    ans += "d" * can_down
    cur_x += can_down
    rest -= can_down * 2
    
    ans += "l" * dic["l"]
    cur_y -= dic['l']
    
    can_left = min(cur_y - 1, rest // 2)
    ans += "l" * can_left
    cur_y -= can_left
    rest -= can_left * 2
    
    can_repeat = rest // 2
    ans += 'rl' * can_repeat
    
    ans += "r" * dic["r"]
    ans += "r" * can_left
    
    ans += "u" * dic["u"]
    ans += "u" * can_down
    
    return ans
    
    
        