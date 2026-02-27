def solution(scores):
    x, y = scores[0]
    n = len(scores)

    scores.sort(key = lambda x: (-x[0], x[1]))
    ins = []
    
    max_b = -1
    for a, b in scores:
        if b < max_b:
            if a == x and b == y:
                return -1
            continue
        
        max_b = b
        ins.append(a + b)
    total = x + y
    cnt = 0
    for num in ins:
        if total < num:cnt+= 1
    return cnt + 1