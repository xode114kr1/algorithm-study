from itertools import product 

def solution(word):
    word_list = ["A", "E", "I", "O", "U"]
    ans = []
    for i in range(1, 6):
        for comb in product(word_list, repeat = i):
            w = "".join(comb)
            ans.append(w)
    ans.sort()
    return (ans.index(word) + 1)