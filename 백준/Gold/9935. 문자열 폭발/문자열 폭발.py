s = input().rstrip()
boom = input().rstrip()
b_len = len(boom)
last = boom[-1]

stack = []

for c in s:
    stack.append(c)
    if c == last and len(stack) >= b_len:
        if ''.join(stack[-b_len:]) == boom:
            del stack[-b_len:]

print(''.join(stack) if stack else "FRULA")