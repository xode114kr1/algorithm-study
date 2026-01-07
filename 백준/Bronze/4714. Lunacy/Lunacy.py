import sys

for line in sys.stdin:
    w = float(line.strip())
    if w < 0:
        break
    print(f"Objects weighing {w:.2f} on Earth will weigh {w * 0.167:.2f} on the moon.")
