def solution(A, B):
    A.sort()
    B.sort()
    s = 0
    cnt = 0
    for a in A:
        while s < len(B) and a >= B[s]:
            s += 1
        if s >= len(B):
            break
        else:
            # print(a, B[s], s)
            cnt += 1
            s += 1
    
    return cnt