s = input()
idx = 0
cur = 1

while 1:
    for c in str(cur):
        if c == s[idx]:
            idx += 1
            if idx == len(s):
                print(cur)
                exit()
    cur += 1