import math

def solution(n, stations, w):
    ran = 1 + 2 * w
    cur = 0
    cnt = 0
    for sta in stations:
        e = sta - w - 1
        if cur < e:
            cnt += math.ceil((e - cur) / ran)
        cur = sta + w
    if cur < n:
        cnt += math.ceil((n - cur) / ran)
    return cnt