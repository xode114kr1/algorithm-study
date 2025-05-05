n = int(input())
count = 0
m_lst = []
def h(st, tmp, nd ,n):
    global count
    if n == 0:
        return
    count += 1
    h(st, nd, tmp, n - 1)
    m_lst.append((st, nd))
    h(tmp, st, nd, n - 1)

h(1, 2, 3, n)
print(count)
for move in m_lst:
    print(move[0], move[1])