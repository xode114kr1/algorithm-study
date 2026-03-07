s = input()
n = len(s)
c = s.count("a")


cnt = s[:c].count("b")
ans = cnt
s = s + s

for i in range(n - 1):
    left, right = i, i + c
    if s[left] == "b":
        cnt -= 1
    if s[right] == "b":
        cnt += 1
    ans = min(ans, cnt)
print(ans)