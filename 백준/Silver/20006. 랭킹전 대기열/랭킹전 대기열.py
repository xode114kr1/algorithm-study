import sys
input = sys.stdin.readline

def find_room(level):
    for i in range(len(room)):
        left, right = between[i]
        if left <= level <= right and len(room[i]) < m:
            return i
    return -1

def make_room(level, name):
    left = max(1, level - 10)
    right = min(501, level + 10)
    between.append([left, right])
    room.append([[level, name]])
    return len(room) - 1

p, m = map(int, input().split())
between = []
room = []
for _ in range(p):
    l, n = input().split()
    l = int(l)

    idx = find_room(l)
    if idx == -1:
        idx = make_room(l, n)
    else:
        room[idx].append([l, n])


for r in room:
    if len(r) == m:
        print("Started!")
    else:
        print("Waiting!")
    r.sort(key = lambda x:x[1])
    for l, n in r:
        print(l, n)
