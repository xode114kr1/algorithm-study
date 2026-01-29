def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x : (x[col - 1], -x[0]))
    lst = []
    for i in range(row_begin - 1, row_end):
        cnt = 0
        for num in data[i]:
            cnt += num % (i + 1)
        lst.append(cnt)
    ans = lst[0]
    for num in lst[1:]:
        ans = ans ^ num

    return ans