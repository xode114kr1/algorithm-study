import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set()
for _ in range(n):
    st = input().strip()
    s.add(st)

for _ in range(m):
    blog_lst = input().strip().split(",")
    for word in blog_lst:
        s.discard(word)
    print(len(s))