from itertools import combinations

def solution(n, q, ans):
    ans_len = len(ans)
    idx_list = [x for x in range(1, n + 1)]
    answer = 0
    for comb in combinations(idx_list, 5):
        isMatch = True
        for idx in range(ans_len):
            
            if len(set(comb) & set(q[idx])) != ans[idx]:
                isMatch = False
                break
        if isMatch:answer += 1

    return answer