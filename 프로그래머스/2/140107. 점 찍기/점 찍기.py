import math

def solution(k, d):
    # x ^ 2 + y ^ 2 <= d ^ 2
    ans = 0
    for x in range(0, d + 1, k):
        y = math.sqrt(d ** 2 - x ** 2)
        added = y // k + 1
        ans += int(added)
    return ans