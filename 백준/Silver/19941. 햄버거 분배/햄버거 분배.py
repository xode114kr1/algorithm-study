n, k = map(int, input().split())
lst = list(input())
ham_lst = [0] * n
for i, c in enumerate(lst):
    if c == "P":
        st = i - k
        en = i + k + 1
        if st < 0 : st = 0
        if en > n  : en = n
        for idx in range(st, en):
            if lst[idx] == "H" and ham_lst[idx] == 0:
                ham_lst[idx] = 1
                break


print(sum(ham_lst))