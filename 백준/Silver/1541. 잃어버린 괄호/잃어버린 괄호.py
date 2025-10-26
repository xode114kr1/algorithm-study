st = input()
only_plus = st.split("-")
first_num = sum(map(int,only_plus[0].split("+")))

if len(only_plus) > 1:
    for mm in only_plus[1:]:
        first_num -= sum(map(int, mm.split('+')))

print(first_num)