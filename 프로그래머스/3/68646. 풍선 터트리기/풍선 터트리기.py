def solution(a):
    # idx를 기준으로 [:idx], [idx + 1 :] 범위에서 idx보다 작은게 1개 이하면 가능
    n = len(a)
    cnt = [0] * n
    l_min = a[0]
    for idx, num in enumerate(a):
        if num > l_min:
            cnt[idx] += 1
        else:
            l_min = num
    r_min = a[-1]
    for idx, num in enumerate(a[::-1]):
        i = n - idx - 1
        if num > r_min:
            cnt[i] += 1
        else:
            r_min = num
    ans = sum(1 for x in cnt if x < 2 )
    return ans