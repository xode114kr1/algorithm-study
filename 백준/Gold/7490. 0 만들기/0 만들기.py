z = int(input())

def bt(idx, s): # idx 를 1부터 시작하자
    if idx == n:
        t = s.replace(" ", "")
        if eval(t) == 0:
            print(s)
        return

    bt(idx + 1, s + " " + str(lst[idx]))
    bt(idx + 1, s + "+" + str(lst[idx]))
    bt(idx + 1, s + "-" + str(lst[idx]))


for _ in range(z):
    num = int(input())
    lst = [x for x in range(1, num + 1)]
    n = len(lst)
    bt(1, str(lst[0]))
    print()