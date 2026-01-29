import math

def solution(cap, n, deliveries, pickups):
    ans = 0
    d_rem = 0
    p_rem = 0
    for i in range(n - 1, -1, -1):
        d_rem += deliveries[i]
        p_rem += pickups[i]

        if d_rem == 0 and p_rem == 0:
            continue
        cur_cnt = math.ceil(max(d_rem, p_rem) / cap)
        ans += (i + 1) * 2 * cur_cnt

        d_rem -= cur_cnt * cap
        p_rem -= cur_cnt * cap

    return ans