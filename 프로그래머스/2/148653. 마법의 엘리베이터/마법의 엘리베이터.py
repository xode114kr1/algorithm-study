def solution(storey):
    ans = 0
    while storey > 0:
        d = storey % 10
        if d < 5:
            ans += d
            storey -= d
        elif d > 5:
            ans += 10 - d
            storey += d
        else:
            if (storey // 10) % 10 >= 5:
                ans += d
                storey += d
            else:
                ans += d
                storey -= d
        storey = storey // 10
    return ans