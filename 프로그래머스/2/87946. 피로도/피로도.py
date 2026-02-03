from itertools import permutations

def solution(k, dungeons):
    n = len(dungeons)
    lst = [x for x in range(n)]
    ans = 0
    for i in range(1, n + 1):
        for perm in permutations(lst, i):
            life = k
            cnt = 0
            for idx in perm:
                if life >= dungeons[idx][0]:
                    life -= dungeons[idx][1]
                    cnt += 1
                else:
                    break
            ans = max(ans, cnt)
    return ans
            