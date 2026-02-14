def solution(p):
    def ok(s):
        t = ''
        stack = []
        op = 0
        cl = 0
        for i in s:
            if i == '(':
                stack.append(i)
                op += 1
            elif len(stack) > 0:
                stack.pop()
                cl += 1
            else:
                return False
        return op == cl
    
    def invert(s):
        return ''.join('(' if ch == ')' else ')' for ch in s)
    def dic_con(s):
        if ok(s):
            return s
        op = 0
        cl = 0
        
        for i in s:
            if op != 0 and op == cl:
                break
            if i == "(":
                op += 1
            else:
                cl += 1
                
        u = s[:op + cl]
        v = s[op + cl:]
        if ok(u): return u + dic_con(v)
        else: return "(" + dic_con(v) + ")" + invert(u[1:-1])
        
    ans = dic_con(p)
    
    return ans