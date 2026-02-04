def solution(s):
    def check(st):
        stack = []
        for c in st:
            if c == "{" or c == "(" or c == "[":
                stack.append(c)
            else:
                if len(stack) == 0 : return False
                last = stack.pop()
                if  c == "]" and last != "[" : return False
                if  c == "}" and last != "{" : return False
                if  c == ")" and last != "(" : return False
        return not stack
    n = len(s)
    cnt = 0

    for i in range(n):
        new_s = s[i:] + s[:i]
        cnt += check(new_s)
    return cnt