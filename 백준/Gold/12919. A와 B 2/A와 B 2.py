import sys
sys.setrecursionlimit(10**5)

def bt(s):
    if s == goal:
        return 1
    if len(s) >= len(goal):
        return 0

    if s not in goal and s[::-1] not in goal:
        return 0

    if bt(s + "A"):
        return 1
    elif bt((s + "B")[::-1]):
        return 1
    return 0


start = input()
goal = input()

print(bt(start))
