def same_cnt(w1, w2):
    i = 0
    while i < len(w1) and i < len(w2):
        if w1[i] != w2[i]:
            break
        i += 1
    return i, w1[:i]

n = int(input())
lst = [[input(), i] for i in range(n)]

sorted_lst = sorted(lst)

max_cnt = 0
prefixes = set()

for i in range(n - 1):
    w1, idx1 = sorted_lst[i]
    w2, idx2 = sorted_lst[i + 1]
    cnt, same_word = same_cnt(w1, w2)

    if cnt > max_cnt:
        max_cnt = cnt
        prefixes = {same_word}
    elif cnt == max_cnt:
        prefixes.add(same_word)

best = None

for prefix in prefixes:
    picked = []
    for w, idx in lst:
        if w.startswith(prefix):
            picked.append((idx, w))
        if len(picked) == 2:
            break

    if len(picked) == 2:
        if best is None or picked < best:
            best = picked

print(best[0][1])
print(best[1][1])