from collections import Counter

def solution(weights):
    cnt = Counter(weights)
    ans = 0
    
    for w, k in cnt.items():
        ans += k * (k - 1) // 2

        ans += k * cnt[2 * w]

        if (3 * w) % 2 == 0:
            ans += k * cnt[(3 * w)//2]

        if (4 * w) % 3 == 0:
            ans += k * cnt[(4 * w)//3]
    
    return ans
