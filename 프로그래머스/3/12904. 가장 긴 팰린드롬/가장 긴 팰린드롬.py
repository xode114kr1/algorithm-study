def solution(s):
    
    def f1(idx):
        left = idx - 1
        right = idx + 1
        cnt = 1
        while left >= 0 and right < n:
            if s[left] == s[right]:
                cnt += 2
                left -= 1
                right += 1
            else:
                break
        return cnt
    def f2(idx):
        left = idx
        right = idx + 1
        cnt = 0
        while left >= 0 and right < n:
            if s[left] == s[right]:
                cnt += 2
                left -= 1
                right += 1
            else:
                break
        return cnt
    n = len(s)
    ans = 0
    for i in range(n):
        ans = max(ans, f1(i), f2(i))
    
    return ans
