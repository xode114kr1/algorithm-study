from itertools import permutations

def solution(expression):
    ans = 0
    def calc(expr, oper, cnt): # oper : dic = {0 : "*", 1 : "+", 2 : "-"} 이런 느낌
        if cnt == 0:
            return eval(expr)
        splited_exprs = expr.split(oper[cnt])
        init = ""
        for splited_expr in splited_exprs:
            init += str(calc(splited_expr, oper, cnt - 1)) + oper[cnt]
        init = init[:-1]
        return eval(init)
        
    lst = ["-", "+", "*"]
    for perm in permutations(lst, 3):
        ans = max(ans, abs(calc(expression, list(perm), 2)))
    return ans
    