def solution(s):
    st = []
    for c in s:
        st.append(c)
        
        while len(st) >= 2:
            if st[-1] == st[-2]:
                st.pop()
                st.pop()
            else:
                break
    if st:
        return 0
    else:
        return 1