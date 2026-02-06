def solution(s):
    s = s[1:-1]
    s = s.split("},{")
    lst = []
    s2 = set()
    ans = []
    for tp in s:
        tp = tp.replace("{","")
        tp = tp.replace("}","")
        lst.append(list(map(int, tp.split(","))))
        
    lst.sort(key= lambda x : len(x))
    
    for l in lst:
        s1 = set(l)
        a = list(s1 - s2)[0]
        s2.add(a)
        ans.append(a)
    return ans