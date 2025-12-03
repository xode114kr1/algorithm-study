import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    N, S = map(int, line.split())
    print(S // (N + 1))