from collections import defaultdict

n, k = map(int, input().split())
lst = list(map(int, input().split()))
dic = defaultdict(list)
st = 0
ans = 0

for idx, i in enumerate(lst):
    dic[i].append(idx)
    if len(dic[i]) > k:
        bad_idx = dic[i][-k - 1]
        st = max(st, bad_idx + 1)

    ans = max(ans, idx - st + 1)
print(ans)