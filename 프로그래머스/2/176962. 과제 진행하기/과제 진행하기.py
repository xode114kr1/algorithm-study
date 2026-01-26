def solution(plans):
    n = len(plans)
    lst = []
    for schedule, start, time in plans:
        h, m = map(int, start.split(":"))
        lst.append((schedule, h * 60 + m, int(time)))
    lst.sort(key = lambda x : x[1])

    stack = []
    ans = []

    for i in range(n - 1):
        schedule, start, time = lst[i]
        next_start = lst[i + 1][1]
        gap = next_start - start

        stack.append([schedule, time])

        while stack and gap > 0:
            top_schedule, top_time = stack.pop()

            if top_time <= gap:
                gap -= top_time
                ans.append(top_schedule)
            else:
                stack.append([top_schedule, top_time - gap])
                gap = 0
    stack.append([lst[-1][0], lst[-1][1]])

    while stack:
        ans.append(stack.pop()[0])
    return ans