def solution(numbers):
    lst = []
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            lst.append(numbers[i] + numbers[j])
    ans = sorted(list(set(lst)))
    return ans