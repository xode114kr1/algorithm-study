def isGroupWord(word):
    before = word[0]
    s = set()
    s.add(before)
    for c in word:
        if c == before:
            continue
        if c in s:
            return False
        before = c
        s.add(c)
    return True

n = int(input())
words = [input() for _ in range(n)]
cnt = 0

for word in words:
    if (isGroupWord(word)):
        cnt += 1
print(cnt)