n = int(input())
count = 0
s = set()
for i in range(n):
    c = input()
    if c == 'ENTER':
        s.clear()
    else:
        if c in s:
            continue
        s.add(c)
        count += 1
print(count)
