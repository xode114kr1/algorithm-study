def solution(s):
    cnt = 0

    while s:
        f = s[0]
        f_cnt = 1
        o_cnt = 0

        split_idx = 0

        for i in range(1, len(s)):
            if s[i] == f:
                f_cnt += 1
            else:
                o_cnt += 1

            if f_cnt == o_cnt:
                split_idx = i
                break
        else:
            cnt += 1
            break

        s = s[split_idx + 1:]
        cnt += 1

    return cnt