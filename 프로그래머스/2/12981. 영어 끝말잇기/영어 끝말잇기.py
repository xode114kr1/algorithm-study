def solution(n, words):
    before = words[0][-1]
    s = set()
    s.add(words[0])
    for i, word in enumerate(words[1:]):
        if before != word[0] or word in s:
            print(i, word)
            return [((i + 1) % n) + 1, (i + 1) // n + 1]
        before = word[-1]
        s.add(word)
    return [0, 0]