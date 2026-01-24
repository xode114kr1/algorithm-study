import math

def solution(r1, r2):
    large = r2 * r2
    small = r1 * r1
    cnt = 0
    for i in range(1, r2 + 1):
        mid = i * i
        y_max = math.floor(math.sqrt(large - mid))
        y_min = 0
        if i < r1:
            y_min = math.ceil(math.sqrt(small - mid))
        added = math.floor(y_max - y_min + 1) 
        # print(y_max, y_min, added)
        cnt += added
    
    return cnt * 4