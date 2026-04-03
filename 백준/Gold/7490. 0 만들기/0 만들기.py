z = int(input())

def c_eval(s):
    s = s.replace(" ", "")
    s = s.replace("-", "+-")
    l = list(map(int, s.split("+")))
    return sum(l)

def bt(idx, s): # idx 를 1부터 시작하자
    if idx == n:
        if c_eval(s) == 0:
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