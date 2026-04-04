s = input()
boom = list(input())
b_len = len(boom)
last = boom[-1]

ans = []
for idx, c in enumerate(s):
    ans.append(c)
    if c == last and ans[-b_len:] == boom:
        del ans[-b_len:]
if ans:
    print(''.join(ans))
else:
    print("FRULA")