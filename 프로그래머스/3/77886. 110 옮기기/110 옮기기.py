#110보다 뒤는 111밖에 없음

def solution(lists):
    ans = []
    for s in lists:
        st = ""
        cnt = 0
        for c in s:
            st += c
            if len(st) >= 3 and st[-3:] == "110":
                cnt += 1
                st = st[:-3]
        idx = st.rfind("0")
        if idx == -1:
            ans.append("110" * cnt + st)
        else:
            s_ans = st[:idx + 1] + "110" * cnt + st[idx + 1:]
            ans.append(s_ans)
    return ans
            