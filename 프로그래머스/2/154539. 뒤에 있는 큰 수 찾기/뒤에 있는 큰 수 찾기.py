def solution(numbers):
    ans = []
    stack = []

    for num in numbers[::-1]:
        before = -1
        while stack:
            last = stack.pop()
            if last > num:
                before = last
                stack.append(last)
                break
        stack.append(num)
        ans.append(before)
    return ans[::-1]