from collections import defaultdict

T = int(input())

for _ in range(T):
    s = input()
    n = int(input())
    min_cnt = float('inf')
    max_cnt = 0

    dic = defaultdict(list)
    for idx, c in enumerate(s):
        dic[c].append(idx)
        if len(dic[c]) >= n:
            s_idx = dic[c][-n]
            e_idx = dic[c][-1]
            gap = e_idx - s_idx + 1
            min_cnt = min(min_cnt, gap)
            max_cnt = max(max_cnt, gap)
    if max_cnt == 0:
        print(-1)
    else:
        print(min_cnt, max_cnt)


