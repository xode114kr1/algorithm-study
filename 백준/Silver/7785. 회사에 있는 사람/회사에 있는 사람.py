n = int(input())

s = set()
for i in range(n):
    name, oper = input().split()
    if oper == 'enter':
        s.add(name)
    elif oper == "leave":
        s.discard(name)
ans = sorted(s, reverse=True)
for i in ans:
    print(i)