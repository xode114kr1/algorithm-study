def solution(n):
    b_n = bin(n)[2:]
    b_n = "0" + b_n
    n_len = len(b_n)
    flag = False
    i = 0
    z_cnt = 0
    o_cnt = 0
    for idx, c in enumerate(b_n[::-1]):
        if c == "0":
            z_cnt += 1
            if flag:
                i = n_len - idx
                break
        if c == "1":
            o_cnt += 1
            if flag == False:
                flag = True
    
    ns = "0b" + b_n[:i - 1] + "1" + "0" * z_cnt + "1" * (o_cnt - 1)
    return (int(ns, 2))