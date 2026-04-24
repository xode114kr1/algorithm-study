import math

def solution(brown, yellow):
    # (x - 2) * (y - 2) = yellow => xy = 2(x + y) + ye - 4
    # 2x + 2y - 4 = brown => y = br // 2 - x + 2
    # x(br // 2 - x + 2) = br + ye
    
    S = brown // 2 + 2
    P = brown + yellow

    D = S * S - 4 * P

    x = (S + math.isqrt(D)) // 2
    y = (S - math.isqrt(D)) // 2

    return [x, y]