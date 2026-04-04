s = input()
boom = list(input())
b_len = len(boom)

ans = []
for idx, c in enumerate(s):
    ans.append(c)
    while ans[-b_len:] == boom:
        del ans[-b_len:]
if ans:
    print(''.join(ans))
else:
    print("FRULA")