from collections import defaultdict

def count(w):
    dic = defaultdict(int)
    for c in w:
        dic[c] += 1
    return dic

n = int(input())
word = input()
words = [input() for _ in range(n - 1)]

cnt1 = count(word)

ans = 0
for w in words:
    cnt2 = count(w)
    for key in cnt1:
        cnt2[key] = abs(cnt2[key] - cnt1[key])
    diff = sum(cnt2.values())
    if diff <= 1:
        ans += 1
    elif diff == 2 and len(word) == len(w):
        for v in cnt2.values():
            if v == 1:
                ans += 1
                break

print(ans)