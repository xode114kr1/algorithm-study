from collections import Counter

n = input()
count = Counter(n)
zero_cnt = count['0'] // 2
one_cnt = count['1'] // 2
idx = 0
tmp = ""
ans = ""
for c in n:
    if c == '1' and one_cnt > 0:
        one_cnt -= 1
        continue
    else:
        tmp += c

for c in tmp[::-1]:
    if c == '0' and zero_cnt > 0:
        zero_cnt -= 1
        continue
    else:
        ans += c
print(ans[::-1])
