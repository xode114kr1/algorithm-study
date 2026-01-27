def solution(book_time):
    lst = []
    cur = -1
    ans = 0
    cnt_lst = [0] * (24 * 60)
    for start, end in book_time:
        st_h, st_m = map(int, start.split(":"))
        en_h, e_m = map(int, end.split(":"))
        lst.append([st_h * 60 + st_m, min(en_h * 60 + e_m + 10, 23 * 60 + 59)])
    lst.sort(key = lambda x : x[1])
    for s, e in lst:
        for i in range(s + 1, e + 1):
            cnt_lst[i] += 1
    return max(cnt_lst)