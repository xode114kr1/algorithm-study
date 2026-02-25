def solution(sequence):
    def max_prefix(lst):
        best = cur = lst[0]
        for x in lst[1:]:
            cur = max(x, x + cur)
            best = max(best, cur)
        return best
    lst1 = [ x * -1 if i % 2 == 0 else x for i, x in enumerate(sequence)]
    lst2 = [ x * -1 if i % 2 == 1 else x for i, x in enumerate(sequence)]
    return max(max_prefix(lst1), max_prefix(lst2))
        