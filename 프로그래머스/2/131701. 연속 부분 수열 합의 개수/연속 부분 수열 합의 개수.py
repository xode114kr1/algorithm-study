def solution(elements):
    n = len(elements)
    s = set()
    for i in range(1, n + 1):
        temp = elements + elements
        prefix = sum(temp[0:i])
        s.add(prefix)
        for j in range(n):
            prefix -= temp[j]
            prefix += temp[i + j]
            s.add(prefix)
    return len(s)