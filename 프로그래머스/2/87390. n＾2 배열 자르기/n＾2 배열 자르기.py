def solution(n, left, right):
    def find_idx(num):
        d = num // n + 1
        r = num % n + 1
        return max(d, r)
    lst = []
    
    for i in range(left, right + 1):
        lst.append(find_idx(i))
    return lst