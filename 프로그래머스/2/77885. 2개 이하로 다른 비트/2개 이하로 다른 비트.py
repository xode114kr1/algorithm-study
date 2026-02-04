def solution(numbers):
    ans = []
    for num in numbers:
        if num == 0:
            ans.append(1)
            continue
        
        st = "0" + bin(num)[2:]
        st = st[::-1]
        n = len(st)
        # 1개 바꾸는거 0 -> 1
        # 2개 바꾸는거 01 -> 10
        # 2개 찾아서 min return
        rep_one = st.replace("0", "1", 1)
        rep_two = st.replace("10", "01", 1)
        rep_one = "0b" + rep_one[::-1]
        rep_two = "0b" + rep_two[::-1]
        ans.append(min(int(rep_one, 2), int(rep_two, 2)))
    return ans
        
    
        
            