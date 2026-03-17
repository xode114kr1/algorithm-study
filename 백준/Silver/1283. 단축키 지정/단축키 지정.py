n = int(input())

def find_first_str(s):
    for idx, c in enumerate(s):
        c = c.lower()
        if idx == 0 or s[idx - 1] == " ":
            if c not in dic:
                dic[c] = (idx, s)
                print(s[:idx] + "[" + s[idx] + "]" + s[idx + 1:])
                return True
    return False

def find_all_str(s):
    for idx, c in enumerate(s):
        if c == " ": continue
        c = c.lower()
        if c not in dic:
            dic[c] = (idx, s)
            print(s[:idx] + "[" + s[idx] + "]" + s[idx + 1:])
            return True
    return False

dic = {}
for i in range(n):
    s = input()
    if find_first_str(s): continue
    elif find_all_str(s): continue
    else:print(s)