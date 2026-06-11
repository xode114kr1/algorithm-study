def solution(keymap, targets):
    min_press = {}

    for key in keymap:
        for i, char in enumerate(key):
            count = i + 1
            if char not in min_press or count < min_press[char]:
                min_press[char] = count

    answer = []

    for target in targets:
        total = 0

        for char in target:
            if char not in min_press:
                total = -1
                break

            total += min_press[char]

        answer.append(total)

    return answer