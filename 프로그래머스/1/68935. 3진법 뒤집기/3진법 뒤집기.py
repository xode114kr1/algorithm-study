def solution(n):
    lst = []
    ans = 0
    while n > 0:
        lst.append(n % 3)
        n = n // 3
    for idx, i in enumerate(lst[::-1]):
        ans += (3**idx) * i
    return ans